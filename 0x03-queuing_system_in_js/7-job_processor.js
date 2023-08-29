const kue = require('kue');

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phone, message, job, done) {
    job.progress(0, 100);
    if (blacklist.includes(phone)) {
       done(new Error(`Phone number ${phone} is blacklisted`));
    }
    else {
        job.progress(50, 100);
        console.log(`Sending notification to ${phone}, with message: ${message}`);
        done();
    }
}

const queue = kue.createQueue();
queue.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
