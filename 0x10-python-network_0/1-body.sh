#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a GET request to the URL and display the body of the response for a 200 status code
response=$(curl -s -w "%{http_code}" $url)

# Extract the status code from the response
status_code=$(tail -c 3 <<< "$response")

# Check if the status code is 200
if [ $status_code -eq 200 ]; then
	# Display the body of the response
	body=$(sed '$s/.$//' <<< "$response")  # Remove the last character (status code) from the response
	echo "$body"
else
	echo "Unexpected status code: $status_code"
fi

