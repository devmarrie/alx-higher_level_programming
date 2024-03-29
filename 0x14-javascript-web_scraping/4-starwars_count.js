#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const toJs = JSON.parse(body).results;
    let count = 0;
    for (const x in toJs) {
      const chars = toJs[x].characters;
      for (const charIndex in chars) {
        if (chars[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
