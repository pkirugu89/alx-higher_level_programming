#!/usr/bin/node
const fs = require('fs');
const fl = process.argv[2];

function readPrint (file) {
  fs.readFile(fl, 'utf-8', function (error, data) {
    if (error) {
      console.log(error);
    } else {
      console.log(data);
    }
  });
}
readPrint(fl);
