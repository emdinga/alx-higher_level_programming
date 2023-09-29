#!/usr/bin/python3
"""  script that takes in a URL and an email, sends 
a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({"email": email}).encode("utf-8")
req = urllib.request.Request(url, data=data, method="POST")

try:
    with urllib.request.urlopen(req) as response:
        content = response.read().decode("utf-8")
        print(content)
except urllib.error.URLError as e:
    print("Error:", e.reason)

