#!/usr/bin/node
// Star wars movies fetched via ajax
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    success: function (data) {
      data.results.forEach(function (movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
