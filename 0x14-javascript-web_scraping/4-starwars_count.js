#!/usr/bin/node
const request = require('request');

function movieCountChar (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Failed to get data. Status code: ' + response.statusCode);
      return;
    }
    try {
      const films = JSON.parse(body).results;
      const wam = films.filter(film =>
        film.characters.some(character => character.includes('/18/'))
      );
      console.log(wam.length);
    } catch (parseError) {
      console.error('Failed to parse JSON response: ', parseError);
    }
  });
}
const apiUrl = process.argv[2];
movieCountChar(apiUrl);
