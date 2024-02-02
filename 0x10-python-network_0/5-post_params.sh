#!/bin/bash
# Bash script takes a URL, send POSt request passed in URL and displays reponse body
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
