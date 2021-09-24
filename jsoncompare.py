from jsondiff import diff
import json


with open('prevJson.json') as infile:
    notajson = infile.read().replace('\n', '')
print(f'notajson type:\n{type(notajson)}\n')


with open('prevJson.json') as infile:
    data1 = json.loads(infile.read().replace('\n', ''))
with open('newJson.json') as infile:
    data2 = json.loads(infile.read().replace('\n', ''))
print(f'data1 type:\n{type(data1)}\n')


difference = diff(data1, data2)
print(difference)
