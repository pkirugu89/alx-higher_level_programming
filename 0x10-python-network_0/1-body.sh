#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of a 200 status code response
curl -s "$1" -o /dev/null -w "%{http_code}" | grep -q ^200 && curl -s "$1"
