const kue = require('kue');


const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];


const push_notification_code_2 = kue.createQueue();

for (let job of jobs) {
    const queuedJob = push_notification_code_2.create('phone', job).save((err) => {
        if (!err) {
            console.log(`Notification job created: ${queuedJob.id}`);
        }
    });
    
    queuedJob.on('complete', (result) => {
        console.log(`Notification job #${queuedJob.id} completed`);
    });

    queuedJob.on('failed', (err) => console.log(`Notification job #${queuedJob.id} failed: ${err}`));

    queuedJob.on('progress', (progress, data) => {
        console.log(`Notification job #${queuedJob.id} ${progress}% complete`);
    });
}
