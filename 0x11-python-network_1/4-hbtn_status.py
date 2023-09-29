#!/usr/bin/python3
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')

print("\t- type:", type(r.text))
print("\t- content:", r.text)
