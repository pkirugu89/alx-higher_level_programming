#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

function movieTitle (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const jsonDict = JSON.parse(body);
      console.log(jsonDict.title);
    }
  });
}
movieTitle(url);
