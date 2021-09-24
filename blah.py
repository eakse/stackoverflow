import json
import csv


output_dict = {}


def str2bool(input: str) -> bool:
    """simple check to see if a str is a bool"""
    # shamelessly stolen from:
    # https://stackoverflow.com/a/715468/9267296
    return input.lower() in ("yes", "true", "t", "1")


def findValue(
    json_obj,
    target_key,
    output_key,
    criteria_key=None,
    criteria_value=False,
    return_key="",
):
    """Finds a specific key 

    Args:
        json_obj ([type]): [description]
        target_key ([type]): [description]
        output_key ([type]): [description]
        criteria_key ([type], optional): [description]. Defaults to None.
        criteria_value (bool, optional): [description]. Defaults to False.
        return_key (str, optional): [description]. Defaults to "".
    """
    # ^^ use PEP standard for docstrings:
    # https://www.python.org/dev/peps/pep-0257/#id16

    # you need to global the output_dict to avoid weirdness
    # see https://www.w3schools.com/python/gloss_python_global_scope.asp
    global output_dict

    for key in json_obj:
        if isinstance(json_obj[key], dict):
            findValue(json_obj[key], target_key, output_key)

        # in this case I advise to use "elif" instead of the "else: if..."
        elif target_key == key:
            #
            if isinstance(json_obj[key], list):
                # so this is the actual logic change.
                for item in json_obj[key]:
                    if (
                        criteria_key != None
                        and criteria_key in item
                        and item[criteria_key] == criteria_value
                    ):
                        output_dict[output_key] = item[return_key]
                        # here you could put a return
            else:
                # this part doesn't change
                output_dict[output_key] = json_obj[key]
                # since we found the key and added in the output_dict
                # you can return here to slightly speed up the total
                # execution time
                return


# Opens and parses json file
with open("source_data.json") as sourcefile:
    json_obj = json.load(sourcefile)


# Opens and parses csv file (mapping)
with open("inputoutput.csv") as csvfile:
    fr = csv.reader(csvfile)
    for row in fr:
        # this check is to determine if you need to add criteria
        # row[2] would be the key to check
        # row[3] would be the value that the key need to have
        # row[4] would be the key for which to return the value
        if row[2] != "":
            findValue(json_obj, row[0], row[1], row[2], str2bool(row[3]), row[4])
        else:
            findValue(json_obj, row[0], row[1])


# Creates/writes into json file
with open("output.json", "w") as out:
    json.dump(output_dict, out, indent=4)
