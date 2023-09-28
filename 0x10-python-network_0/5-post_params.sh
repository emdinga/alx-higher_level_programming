#!/bin/bash
# Set the POST data with email and subject parameters and send a POST request
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
