import os
import requests

# See link down below to generate your Private Access Token
personal_access_token = '42muadbwmvihps424suvtvkv4fyu2p6szetxn4jookffvc4y45sq'
url = 'https://dev.azure.com/tpwange/_apis/projects?api-version=6.1-preview.4'

data = [
 {
 "op": "add",
 "path": "/fields/System.Title",
 "value": "Sample task"
 }
]

r = requests.get(url, json=data, 
    headers={'Content-Type': 'application/json-patch+json'},
    auth=('', personal_access_token))

print(r.json())