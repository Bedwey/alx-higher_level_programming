#!/bin/bash
# sends a POST, displays the body of the response.
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1" -X POST
