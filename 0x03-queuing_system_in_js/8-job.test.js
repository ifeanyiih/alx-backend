import createPushNotificationsJobs from './8-job.js';
const kue = require('kue');
const chai = require('chai');
const assert = require('assert');
let queue;


describe('createPushNotificationsJobs', () => {
    before(function() {
        queue = kue.createQueue();
        queue.testMode.enter();
    });
 
    afterEach(function() {
        queue.testMode.clear();
    });
 
    after(function() {
        queue.testMode.exit();
    });

    const jobs = [
            {phoneNumber: '4132345746', message: 'This is the code 1234'},
            {phoneNumber: '38465930037', message: 'This is the code 5678'}    
        ];



    it('display a error message if jobs is not an array', (done) => {
        try{
            createPushNotificationsJobs('jobs', queue);
        } catch (e) {
            assert(e.message === 'Jobs is not an array');
            assert(e.name === 'Error');
        }
        done();
    });

    it('create two new jobs to the queue', (done) => {
        createPushNotificationsJobs(jobs, queue);
        chai.expect(queue.testMode.jobs.length).to.equal(2);
        chai.expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        chai.expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
        done();
    });
});
