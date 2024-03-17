#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

function taskCountDone (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Failed to get data. Status code: ', response.statusCode);
      return;
    }

    const todos = JSON.parse(body);
    const doneTasks = {};

    todos.forEach(task => {
      if (task.completed) {
        if (!doneTasks[task.userId]) {
          doneTasks[task.userId] = 1;
        } else {
          doneTasks[task.userId]++;
        }
      }
    });
    console.log(doneTasks);
  });
}
taskCountDone(url);
