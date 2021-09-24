import os
from datetime import datetime


def get_files_from_path(path: str) -> list:
    result = []
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename

            if filename.startswith('Logs_') and filename.endswith('.tar.xz'):
                result.append(filepath)
    return result    


def get_old_files(filelist: list, max_days=184) -> list:
    currentdate = datetime.now()
    result = []
    for file in filelist:
        datestr = file.split('Logs_')[1].split('.tar.xz')[0]
        filedate = datetime.strptime(datestr, '%d%m%Y')
        tdelta = currentdate - filedate
        if tdelta.days > max_days:
            result.append(file)
    return result


def delete_files(filelist: list):
    for file in filelist:
        os.remove(file)


allfiles = get_files_from_path('testing')
oldfiles = get_old_files(allfiles)

delete_files(oldfiles)