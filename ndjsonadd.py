# https://pypi.org/project/ndjson/
# pip install ndjson
import ndjson
import json
from pprint import pprint

with open('path/to/file/im_a_ndjson.ndjson') as infile:
    ndjson_object = ndjson.load(infile)


with open('path/to/file/json_file2.json') as infile:
    dict_object = json.load(infile)


print(type(ndjson_object[0]['frameNumber']))
# output: <class 'int'>


for key in dict_object:
    # int needed as you can see above
    framenumber = int(key.strip('frame'))
    # find the matching ndjson object
    for ndjs in ndjson_object:
        if ndjs['frameNumber'] == framenumber:
            # add the key/value pair
            ndjs[key] = dict_object[key]
            # we can break as we've found it
            break


with open('path/to/file/new_ndjson.ndjson', 'w') as outfile:
    ndjson.dump(ndjson_object, outfile)
