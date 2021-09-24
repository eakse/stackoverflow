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
            # use os.sep to get os independent separator
            filepath = f'{subdir}{os.sep}{fname}'
            if ext == None:
                result.append(filepath)
            elif type(ext) == str and fname.lower().endswith(ext.lower()):
                result.append(filepath)
            elif type(ext) == list:
                for item in ext:
                    if fname.lower().endswith(item.lower()):
                        result.append(filepath)
    return result


directory = "D:\Python\Badge Recovery"
filelist = get_files_from_path(directory)


badgecommandlist = []
for filename in filelist:
    print(f'Reading file: {filename}')
    # I always use the with open
    with open(filename) as infile:
        lines = infile.readlines()  # read content of each file

    for line in lines:
        if (
            "badge give" in line
            or "badge share" in line
            or "badge take" in line
            or "badge leave" in line
            or "badge create" in line
        ):  # check if badge command is in each line
            badgecommandlist.append(line)


pprint(badgecommandlist)
with open("commandlist.txt", "w") as outfile:
    # no need to write line by line as writelines()
    # accepts a list directly
    outfile.writelines(badgecommandlist)
    print(f'File saved to: {outfile.name}')
