#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
    process.exit(1);
  }

  const todos = JSON.parse(body);

  const completedTasksByUser = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (!completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId] = 1;
      } else {
        completedTasksByUser[todo.userId]++;
      }
    }
  }

  for (const userId in completedTasksByUser) {
    console.log(`User ${userId} has completed ${completedTasksByUser[userId]} tasks.`);
  }
});

