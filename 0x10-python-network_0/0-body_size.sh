#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
# get the URL from the cmd line arg
url=$1

# Extract content length from the headers
c_len=$(curl -sI $url | grep -i content-length | awk '{print $2}' | tr -d '\r\n')
# Display the length
echo "$c_len"

