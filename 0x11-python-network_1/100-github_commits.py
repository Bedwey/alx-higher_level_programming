#!/usr/bin/python3
"""Print all commits by: `<sha>: <author name>` (one by line)"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    header = {'X-GitHub-Api-Version': '2022-11-28'}
    r = requests.get(url, headers=header)

    commits = r.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
