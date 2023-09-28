#!/bin/bash
# displays the body of the response.
curl -sLX PUT -H "origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me_3
