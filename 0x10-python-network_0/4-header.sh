#!/bin/bash
# Set the custom header X-School-User-Id with the value 98 & send a GET request
curl -s -H "X-School-User-Id: 98" "$1"
