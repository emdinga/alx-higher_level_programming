#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./7-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
    process.exit(1);
  }

  const movieData = JSON.parse(body);

  console.log(`Characters in "${movieData.title}":`);
  movieData.characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        process.exit(1);
      }

      if (charResponse.statusCode !== 200) {
        console.error(`Request failed with status code: ${charResponse.statusCode}`);
        process.exit(1);
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

