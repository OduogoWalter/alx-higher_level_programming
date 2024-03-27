#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument,
# with the contents of a file (second argument) as the request body,
# and displays the response body.

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 URL FILE"
    exit 1
fi

URL=$1
FILE=$2

curl -sX POST -H "Content-Type: application/json" -d @"$FILE" "$URL"

