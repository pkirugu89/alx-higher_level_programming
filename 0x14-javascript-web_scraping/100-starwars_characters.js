#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failure Status code: ', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  console.log('Characters in', movie.title + ':');
  movie.characters.forEach(cUrl => {
    request(cUrl, (cErr, cResponse, cBody) => {
      if (cErr) {
        console.error('Get Character info error:', cErr);
        return;
      }
      if (cResponse.statusCode !== 200) {
        console.error('Failure Character data status code:', cResponse.statusCode);
        return;
      }

      const character = JSON.parse(cBody);
      console.log(character.name);
    });
  });
});
