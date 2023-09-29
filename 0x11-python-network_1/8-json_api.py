#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import sys
import requests

if __name__ == "__main__":
    try:
        search = sys.argv[1]
    except IndexError:
        search = ""

    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': search})

    try:
        data = r.json()
        if data == {}:
            print('No result')
        else:
            print(f"[{data['id']}] {data['name']}")
    except ValueError:
        print('Not a valid JSON')
