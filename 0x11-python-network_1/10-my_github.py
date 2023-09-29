#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import sys
import requests

if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    header = {'X-GitHub-Api-Version': '2022-11-28'}
    token = requests.auth.HTTPBasicAuth(user, token)

    r = requests.get(url, headers=header, auth=token)
    print(r.json().get('id'))
