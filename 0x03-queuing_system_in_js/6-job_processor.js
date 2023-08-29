const kue = require('kue');

const processorQueue = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

processorQueue.process('data', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});
