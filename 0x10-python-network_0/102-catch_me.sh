#!/bin/bash
# Script to send a request to 0.0.0.0:5000/catch_me that makes the server respond with "You got me!"
curl -sX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98" -L

