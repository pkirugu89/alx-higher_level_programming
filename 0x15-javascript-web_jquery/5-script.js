#!/usr/bin/node
// Add Item to the list
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
