import os
import csv


def get_files_from_path(path: str, extension: str=None) -> list:
    """return list of files from path"""
    # see the answer on the link below for a ridiculously 
    # complete answer for this. I tend to use this one.
    # note that it also goes into subdirs of the path
    # https://stackoverflow.com/a/41447012/9267296
    result = []
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if extension == None:
                result.append(filepath)
            elif filename.lower().endswith('.csv'):
                result.append(filepath)
    return result


def load_csv(filename: str) -> list:
    """load a CSV file and return it as a list of dict items"""
    result = []
    with open(filename) as infile:
        reader = csv.reader(infile)
        # get the column names
        # https://stackoverflow.com/a/28837325/9267296
        # doing this as you state that you're dealing with
        # x/y and x/z values
        column0, column1 = next(reader)

        for line in reader:
            try:
                result.append({column0: float(line[0]), 
                               column1: float(line[1])})
            except Exception as e:
                # I always print out error messages
                # in case of random weird things
                print(e)
                continue

    return result


def load_all(path: str) -> dict:
    """loads all CSV files into a dict"""
    result = {}
    csvfiles = get_files_from_path(path)
    for filename in csvfiles:
        # extract the filename without extension
        # and us it as key name
        # since we only load .csv files we can just
        # remove the last 4 characters from filename
        keyname = os.path.basename(filename)[:-4]
        result[keyname] = load_csv(filename)
    return result


from pprint import pprint
all = load_all('path/to/csv/files')
pprint(all)
print('\n--------------------\n')
pprint(all['11 z 205'])