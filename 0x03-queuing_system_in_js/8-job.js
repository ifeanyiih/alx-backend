function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    for (const job of jobs) {
        const queueJob = queue.create('push_notification_code_3', job);

        queueJob.on('failed', (err) => console.log(`Notification job #${queueJob.id} failed: ${err}`));
        queueJob.on('complete', (result) => console.log(`Notification job #${queueJob.id} completed`));
        queueJob.on('progress', (progress, data) => {
            console.log(`Notification job #${queueJob.id} ${progress}% complete`);
        });

        queueJob.save((err) => {
            if (!err) console.log(`Notification job created: ${queueJob.id}`);
        });

     }
}

module.exports = createPushNotificationsJobs;
