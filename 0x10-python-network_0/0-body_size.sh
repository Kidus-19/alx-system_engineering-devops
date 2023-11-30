#!/bin/bash
# This script takes a URL, sends a request to that URL, and display the size of the body of that response.
curl -w '%{size_download}\n' -o /dev/null -s $1
