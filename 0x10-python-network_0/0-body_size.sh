#!/bin/bash
# displays the size of the body of the response.
curl -w "%{size_download}\n" -o /dev/null -s $1
