#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep "200" &>/dev/null && curl -sL "$1"
