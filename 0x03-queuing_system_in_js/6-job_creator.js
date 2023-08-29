const kue = require('kue');

const job_data = {
  phoneNumber: '0123 456 789',
  message: 'phone Number',
}

const queue = kue.createQueue();
const job = queue.create('push_notification_code', job_data).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
});

job.on('complete', (result) => {
    console.log('Notification job completed');
});

job.on('failed', (err) => {
    console.log('Notification job failed');
});
