const redis = require('redis');
const util = require('util');
const client = redis.createClient();
const getAsync = util.promisify(client.get).bind(client);
const kue = require('kue');
const queue = kue.createQueue();
const express = require('express');
const app = express();
const port = 1245;



function reserveSeat(number) {
    client.set('available_seats', number, redis.print);
}

async function getCurrentAvailableSeats() {
    let available;
    available = await getAsync('available_seats');
    return available;
}

app.get('/available_seats', async (req, res) => {
    const available_seats = await getCurrentAvailableSeats();
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    const data = {"numberOfAvailableSeats": available_seats}
    res.send(JSON.stringify(data));
});

app.get('/reserve_seat', async (req, res) => {
    const reservationStat = await getAsync('reservationEnabled');
    res.setHeader('Content-Type', 'application/json');
    if (!+reservationStat) {
        res.statusCode = 403;
        const response = { "status": "Reservation are blocked" };
        res.send(JSON.stringify(response));
    } else {
        res.statusCode = 200;
        const job = queue.create('reserve_seat', {"seat": 1});
        job.save((err) => {
            if (!err) {
                const data = { "status": "Reservation in process" };
                res.send(JSON.stringify(data));
            } else {
                const data = { "status": "Reservation failed" };
                res.send(JSON.stringify(data)); 
            }
        });
        job.on('complete', (result) => {
            console.log(`Seat reservation job ${job.id} completed`);
        });
        job.on('failed', (err) => console.log(`Seat reservation job #${job.id} failed: ${err}`));
    }
});

app.get('/process', async (req, res) => {
    queue.process('reserve_seat', async (job, done) => {
        const current_available_seats = await getCurrentAvailableSeats();
        const available_seats = current_available_seats - 1;
        reserveSeat(available_seats);
        if (available_seats == 0) {
            client.set('reservationEnabled', 0);
        }
        if (available_seats >= 0) {
            done();
        } else {
            done(new Error('Not enough seats available'));
        }
    });

    const data = { "status": "Queue processing" };
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(data));
});

// reserves 50 seats
reserveSeat(50);

// reservation is enabled
client.set('reservationEnabled', 1);

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
