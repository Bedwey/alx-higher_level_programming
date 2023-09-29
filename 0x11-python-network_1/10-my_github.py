#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    header = {'X-GitHub-Api-Version': '2022-11-28', 'Accept': 'application/vnd.github+json'}
    token = HTTPBasicAuth(user, token)

    r = requests.get(url, headers=header, auth=token)
    print(r.json().get('id'))
