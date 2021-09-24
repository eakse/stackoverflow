import csv
from pprint import pprint
import json


# load gpo_full.csv into a list of dict using
# csv.DictReader & list comprehension
with open("path/to/file/gpo_full.csv") as infile:
    gpo_full = [item for item in csv.DictReader(infile)]
# pprint(gpo_full)


# do the same for CAP_cols.csv
with open("path/to/file/CAP_cols.csv") as infile:
    cap_cols = [item for item in csv.DictReader(infile)]
# pprint(cap_cols)


def match_topic(gpo_topic: str, cap_topic: str) -> bool:
    """We need a function as some of the mapping is not simple

    Args:
        gpo_topic (str): gpo topic
        cap_topic (str): CAP topic

    Returns:
        bool: True if topics match
    """
    # this one is simple
    if gpo_topic in cap_topic:
        return True
    # you need to repeat the below conditional check
    # for each custom topic matching
    elif gpo_topic == "weather" and cap_topic == "rain & cloudy":
        return True 
    # example secondary topic matching
    elif gpo_topic == "foo" and cap_topic == "bar":
        return True 
    # finally return false for no matches
    return False


# we need this later
gpo_length = len(gpo_full)
results = []
cap_left_over = []
# do the actual mapping
# this could've been done above, but I separated it intentionally
for cap in cap_cols:
    found = False
    # first find the corresponding gpo
    for index, gpo in enumerate(gpo_full):
        if (
            gpo["Specific_Date"] == cap["Specific_Date"] # check by date
            and match_topic(gpo["topic"], cap["topic"]) # check if topics match
        ):
            results.append({
                "Date": gpo["Date"],
                "Specific_Date": gpo["Specific_Date"],
                "Topic": {
                    "GPO": gpo["topic"],
                    "CAP": cap["topic"]
                },
                "GPO": {
                    "hearing_sub_type": gpo["hearing_sub_type"]
                },
                "CAP": {
                    "majortopic": cap["majortopic"],
                    "id": cap["id"],
                    "Chamber": cap["Chamber"]
                }
            })
            # pop & break to remove the gpo item
            # this is so you're left over with a list of
            # gpo items that didn't match
            # it also speeds up further matches
            gpo_full.pop(index)
            found = True
            break
    # this is to check if there's stuff left over
    if not found:
        cap_left_over.append(cap)


with open('path/to/file/combined_json.json', 'w') as outfile:
    json.dump(results, outfile, indent=4)


pprint(results)
print(f'\nLength:\n  Results: {len(results)}\n  CAP: {len(cap)}\n  GPO: {gpo_length}')
print('\nLeftover GPO:')
pprint(gpo_full)
print('\nLeftover CAP:')
pprint(cap_left_over)
