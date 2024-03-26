#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, with the contents of a file passed as the second argument

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File not found: $2"
    exit 1
fi

# Check if the file contains valid JSON
if ! jq -e . >/dev/null 2>&1 <"$2"; then
    echo "Not a valid JSON"
    exit 1
fi

# Send the POST request with the JSON content
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
