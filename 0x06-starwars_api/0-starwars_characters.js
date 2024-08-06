#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

function getMovieCharacters (movieId) {
  request(`${API_URL}/films/${movieId}/`, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const characters = JSON.parse(body).characters;
    const characterPromises = characters.map(url =>
      new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      })
    );

    Promise.all(characterPromises)
      .then(names => names.forEach(name => console.log(name)))
      .catch(error => console.error('Promise Error:', error));
  });
}

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  getMovieCharacters(movieId);
}
