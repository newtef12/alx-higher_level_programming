#!/usr/bin/node
const req = require('request');
const endPoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req({ url: endPoint, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
