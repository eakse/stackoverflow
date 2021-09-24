import os
import json
from pprint import pprint


def find_value_by_key(iterable, findkey):
    """recursive method to return the value for the first
    instance of 'findkey'."""
    if type(iterable) == list:
        for item in iterable:
            result = find_value_by_key(item, findkey)
            if result != None:
                    return result
    elif type(iterable) == dict:
        for key in iterable:
            value = iterable[key]
            if key == findkey:
                return value
            elif type(value) == dict or type(value) == list:
                result = find_value_by_key(value, findkey)
                if result != None:
                    return result
    return None



def get_files_from_path(path: str='.', extension=None) -> list:
    """Find files in path and return them as a list.
    Gets all files in folders and subfolders
    
    See the answer on the link below for a ridiculously 
    complete answer for this. I tend to use this one.
    note that it also goes into subdirs of the path
    https://stackoverflow.com/a/41447012/9267296
    Args:
        path (str, optional): Which path to start on. 
                              Defaults to '.'.
        extension (str/list, optional): Optional file extention. 
                                        Defaults to None.

    Returns:
        list: list of full file paths
    """
    result = []
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if extension == None:
                result.append(filepath)
            elif filename.lower().endswith(extension.lower()):
                result.append(filepath)
    return result


filelist = get_files_from_path(extension='.json')
jsonlist = []
for filepath in filelist:
    with open(filepath) as infile:
        jsonlist.append(json.load(infile))

# for js in jsonlist:
#     print(find_value_by_key(js, 'lookupCode'))


# from pprint import pprint
# pprint(jsonlist)


jsondata = json.loads("""{
"created_at": "Fri Oct 12 00:00:00 +0000 2012", "text": "ottimes daily top stories ghostlightning secretanimelov erojunko",
 "user": {"id": 163444845, "followers_count": 853},
 "retweet_count": 0,
 "entities": {"hashtags": [], "user_mentions": []}}
 """)

print(find_value_by_key(jsondata, 'hashtags'))