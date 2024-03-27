// Using css class to change div color to red
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $('HEADER').addClass('red');
  });
});
