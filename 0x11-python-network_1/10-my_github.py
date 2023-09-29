#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id
"""


import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./10-my_github.py <username> <access_token>")
    sys.exit(1)

username = sys.argv[1]
access_token = sys.argv[2]

url = f"https://api.github.com/user"

# Set up the Basic Authentication header with your username and access token
auth = (username, access_token)

response = requests.get(url, auth=auth)

if response.status_code == 200:
    data = response.json()
    print(data.get("id"))
else:
    print(None)

