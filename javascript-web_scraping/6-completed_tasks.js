#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;

  const todos = JSON.parse(body);
  const completedByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId.toString();
      completedByUser[userId] = (completedByUser[userId] || 0) + 1;
    }
  });

  console.log(completedByUser);
});
