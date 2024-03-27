#!/bin/bash
# This script sends a JSON POST request to a URL.
# First argument: URL to send the request to.
# Second argument: Filename of the file containing JSON data to send.

url="$1"
json_file="$2"

curl -s -X POST -H "Content-Type: application/json" -d @"$json_file" "$url"

