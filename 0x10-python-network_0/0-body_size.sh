#!/bin/bash
#takes in a URL, sends a request to that URL and displays the size of the body
curl -s "$1" | wc -c
