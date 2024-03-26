#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response

# Send the request and store the response in a temporary file
curl -s -o response.txt -w "%{http_code}" "$1"

# Extract the status code from the file and display it
cat response.txt
