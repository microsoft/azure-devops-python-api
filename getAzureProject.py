import os
import requests
import json

# See link down below to generate your Private Access Token
personal_access_token = '42muadbwmvihps424suvtvkv4fyu2p6szetxn4jookffvc4y45sq'

#projects
projectList_url = 'https://dev.azure.com/tpwange/_apis/projects?api-version=6.1-preview.4'

#buildListurl = "https://dev.azure.com/{organization}/{project}/_apis/build/builds?api-version=6.1-preview.6"
buildList_url = "https://dev.azure.com/tpwange/poc/_apis/build/builds?api-version=6.1-preview.6"

#buildturl = 'https://dev.azure.com/{organization}/{project}/_apis/build/builds/{buildId}/artifacts?api-version=6.1-preview.5
build_url = "https://dev.azure.com/tpwange/poc/_apis/build/builds/91/artifacts?api-version=6.1-preview.5"

#buildArtifactsListurl = https://dev.azure.com/{organization}/{project}/_apis/build/builds/{buildId}/artifacts?artifactName={artifactName}&api-version=6.1-preview.5"
buildArtifactsList_url = "https://dev.azure.com/tpwange/tpwange/_apis/build/builds/91/artifacts?artifactName='Code Coverage Report_91'&api-version=6.1-preview.5"

data = [
 {
    "op": "add",
    "path": "/fields/System.Title",
    "value": "Sample task"
 }
]

r = requests.get(projectList_url, json=data, 
    headers={'Content-Type': 'application/json-patch+json'},
    auth=('', personal_access_token))

# Serializing json & write to file
json_object = json.dumps(r.json(), indent = 2)
open("export\\projects.json", "w").write(json_object)

print("export to projects.json------------------------------------------")

r = requests.get(buildList_url, json=data, 
    headers={'Content-Type': 'application/json-patch+json'},
    auth=('', personal_access_token))

# Serializing json & write to file
json_object = json.dumps(r.json(), indent = 2)
open("export\\buildList.json", "w").write(json_object)

print("export to buildList.json---------------------------------------------")

r = requests.get(build_url, json=data, 
    headers={'Content-Type': 'application/json-patch+json'},
    auth=('', personal_access_token))

# Serializing json & write to file
json_object = json.dumps(r.json(), indent = 2)
open("export\\build.json", "w").write(json_object)
print("export to build.json---------------------------------------------")

r = requests.get(buildArtifactsList_url, json=data, 
    headers={'Content-Type': 'application/json-patch+json'},
    auth=('', personal_access_token))

# Serializing json & write to file
json_object = json.dumps(r.json(), indent = 2)
open("export\\buildArtifactsList.json", "w").write(json_object)
print("export to buildArtifactsList.json---------------------------------------------")