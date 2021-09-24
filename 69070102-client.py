import requests
import json


with open("credentials.json") as infile:
    credentials = json.load(infile)


target = "http://127.0.0.1:5000/api/query"
asjson = json.dumps(credentials)
print(type(asjson), asjson)
response = requests.post(target, json=asjson)
print(response, response.text)