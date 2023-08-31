#!/bin/bash
# Send a request to the URL and store the response in a variable
curl -s "$1" | wc -c
