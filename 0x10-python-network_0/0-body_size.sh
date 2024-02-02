#!/bin/bash
# Bash script thats a URL, send request to URL and display body response size
curl -sI "$1" | grep -E 'Content-Length' | cut -d' ' -f2
