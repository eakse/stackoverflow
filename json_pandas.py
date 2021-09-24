import os
from pprint import pprint


def get_files_from_path(path: str = ".", ext=None) -> list:
    """Find files in path and return them as a list.
    Gets all files in folders and subfolders

    See the answer on the link below for a ridiculously
    complete answer for this. I tend to use this one.
    note that it also goes into subdirs of the path
    https://stackoverflow.com/a/41447012/9267296
    Args:
        path (str, optional): Which path to start on.
                              Defaults to '.'.
        ext (str/list, optional): Optional file extention.
                                  Defaults to None.

    Returns:
        list: list of full file paths
    """
    result = []
    for subdir, dirs, files in os.walk(path):
        for fname in files:
            filepath = f"{subdir}{os.sep}{fname}"
            if ext == None:
                result.append(filepath)
            elif type(ext) == str and fname.lower().endswith(ext.lower()):
                result.append(filepath)
            elif type(ext) == list:
                for item in ext:
                    if fname.lower().endswith(item.lower()):
                        result.append(filepath)
    return result


def create_recursive_json(filelist: list, result={}):
    for file in filelist:
        if os.sep in file:
            folders = file.split(os.sep)
            result[folders[0]] = folders[0]
            print(result)
            result[folders[0]] = create_recursive_json(
                [os.sep.join(folders[1:])], result
            )
        else:
            result[file] = file
    return result


filelist = get_files_from_path(path="path", ext=".csv")
pprint(filelist)
asjson = create_recursive_json(filelist)
pprint(asjson, indent=4)


{
    "path": [
        {
            "to": [
                {
                    "file": [
                        "mapping.csv", 
                        "gpo_full.csv"
                        ]
                },
                {
                    "csv": [
                        "files"
                    ]
                }
            ]
        }
    ]
}
