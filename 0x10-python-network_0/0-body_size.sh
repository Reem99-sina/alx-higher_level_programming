#!/bin/bash

# Prompt the user to enter a URL
read -p "Enter a URL: " url

# Send a request to the URL and store the response in a variable
response=$(curl -s -o /dev/null -w "%{size_download}" $url)

# Display the size of the response body in bytes
echo "Response size: $response bytes"
