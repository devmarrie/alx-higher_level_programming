#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        const obj = Object.assign(completed, task);
        console.log(obj);
      }
    }
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
