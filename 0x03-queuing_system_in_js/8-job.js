const kue = require('kue');

const push_notification_code_3 = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    for (const job of jobs) {
        const queueJob = push_notification_code_3.create('push notif', job).save((err) => {
            if (!err) console.log(`Notification job created: ${queueJob.id}`);
        });

        queueJob.on('complete', (result) => console.log(`Notification job #${queueJob.id} completed`));
        queueJob.on('failed', (err) => console.log(`Notification job #${queueJob.id} failed: ${err}`));
        queueJob.on('progress', (progress, data) => {
            console.log(`Notification job #${queueJob.id} ${progress}% complete`);
        });
    }
}

module.exports = createPushNotificationsJobs;
