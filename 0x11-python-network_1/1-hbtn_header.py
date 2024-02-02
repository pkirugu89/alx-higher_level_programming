#!/usr/bin/python3
"""
URL that send requests and display value of X-Request-Id.
"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)
