#!/usr/bin/node
// Toggle header content
$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
