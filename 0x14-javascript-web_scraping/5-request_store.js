#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

function displayWebPage (url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to get data. Status code: ' + response.statusCode);
      return;
    }
    writeFilez(filePath, body);
  });
}

function writeFilez (filePath, content) {
  fs.writeFile(filePath, content, 'utf8', (error) => {
    if (error) {
      console.error('Error writing to file: ', error);
    //  return;
    }
    // console.log('Webpage Content successfully stored in: ', filePath);
  });
}
displayWebPage(url, filePath);
