#!/bin/bash
# Bash Script that takes in a URL and displays all HTTP methods the server accepts
curl -sI "$1" | grep "Allow:" | sed 's/Allow: //'
