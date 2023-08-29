import { createClient, print } from 'redis';
const util = require('util');

const client = createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));
client.on('ready', () => console.log('Redis client connected to the server'));


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) console.log(err);
        print(`Reply: ${reply}`);
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) console.log(err);
        print(reply);
    });
}

util.promisify(displaySchoolValue);

(async function () {
    await displaySchoolValue('Holberton');
})();
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
