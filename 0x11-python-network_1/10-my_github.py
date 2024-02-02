#!/usr/bin/python3
""" My Github ! """
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    # Using Basic Authentication with a personal access token
    auth = (username, password)

    response = requests.get(url, auth=auth)

    try:
        user_data = response.json()
        print(user_data.get('id', 'None'))
    except ValueError:
        print("None")
