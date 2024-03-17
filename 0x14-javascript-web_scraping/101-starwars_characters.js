#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
getCharacters(movieId);

function getCharacters (movieId) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
  request(url, (err, response, body) => {
    if (err) {
      console.error('Error:', err);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed data retrieval status code: ', response.statusCode);
      return;
    }
    const movie = JSON.parse(body);
    movie.characters.forEach(cUrl => {
      request(cUrl, (cError, cResponse, cBody) => {
        if (cError) {
          console.error('Error getting character info:', cError);
          return;
        }

        const character = JSON.parse(cBody);
        console.log(character.name);
      });
    });
  });
}
