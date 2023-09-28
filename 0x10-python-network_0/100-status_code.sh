#!/bin/bash
# sends a POST, displays the body of the response.
curl -s -o /dev/null -I -w "%{http_code}" "$1"
