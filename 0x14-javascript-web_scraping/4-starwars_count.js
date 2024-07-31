#!/usr/bin/node

const request = require('request');

// Function to get movies with a specific character
const getMoviesWithCharacter = (apiUrl, characterId) => {
  const url = `${apiUrl}`;

  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
      return;
    }

    try {
      // Parse the JSON response
      const movies = JSON.parse(body).results;

      // Filter movies containing the character
      const moviesWithCharacter = movies.filter(movie => {
        const characterUrls = movie.characters;
        // Corrected: The characterId should be checked against each URL in characterUrls
        return characterUrls.some(url => url.endsWith(`/${characterId}/`));
      });

      console.log(moviesWithCharacter.length);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
};

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node script.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = '18'; // Character ID should be a string
getMoviesWithCharacter(apiUrl, characterId);
