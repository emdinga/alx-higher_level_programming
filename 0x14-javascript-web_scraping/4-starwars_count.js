#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
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

  const filmsData = JSON.parse(body);
  const characterId = '18';


  const moviesWithWedge = filmsData.results.filter((film) =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(moviesWithWedge.length);
});

