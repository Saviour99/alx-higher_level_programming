#!/usr/bin/env node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as an argument.');
  process.exit(1);
}

// Star Wars API base URL
const apiBaseUrl = 'https://swapi.dev/api/films/';

// Construct the URL for the specific movie
const movieUrl = `${apiBaseUrl}${movieId}/`;

// Fetch movie data from the Star Wars API
request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie data. Status code:', response.statusCode);
    process.exit(1);
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Print each character's name
  movieData.characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to retrieve character data. Status code:', response.statusCode);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
