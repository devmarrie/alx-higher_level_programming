#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const toJs = JSON.parse(body);
    console.log(toJs.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
