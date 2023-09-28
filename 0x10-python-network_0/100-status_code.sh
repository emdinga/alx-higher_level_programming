#!/bin/bash
# Send a GET request to the URL using curl and display only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
