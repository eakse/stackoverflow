# download sample file
from pprint import pprint
import requests
url = 'https://tmpfiles.org/dl/74576/coc.text'
r = requests.get(url, allow_redirects=True)
open('text1.txt', 'wb').write(r.content)


def clean_text(text) -> list:
    """Removes empty lines as well as leading and trailing spaces.
    Also removes EOL characters.

    Args:
        text (str/list): Input text

    Returns:
        (list): A list of strings
    """
    if type(text) == str:
        splittext = text.splitlines()
        if len(splittext) == 1:
            print("Text is a single line string")
            return text
    elif type(text) == list:
        splittext = text
    result = []
    for line in splittext:
        cleaned = line.strip()
        if cleaned != "":
            result.append(cleaned)
    return result


import requests
def download_file(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)


url = 'https://tmpfiles.org/dl/74576/coc.text'
filename = 'text_sample1.txt'
download_file(url, filename)


with open(filename) as infile:
    text = infile.read()



sections = text.split('\n \n')
cleaned_sections = []
for section in sections:
    cleaned_sections.append(clean_text(section.splitlines()))


pprint(cleaned_sections)


def find_abn(lines: list) -> str:
    for line in lines:
        if "ABN " and "AFSL " in line:
            abn_split = line.split()
            abn_value = f"{abn_split[1]} {abn_split[2]}"
            return abn_value
    # return None when ABN value not found
    return None


def find_policy_date(lines: list) -> str:
    from datetime import date



previous_line = ""
for line in text:
    # two \ needed due to it being a special character in strings
    if "Policy Number(s)" in previous_line:
        policy_number = line
    elif "From " in line and "Period of Insurance" in previous_line:
        # this is a secondary check for the start/end dates
        # Just in case another line in the text contains 'From '
        start = line.split("From ")[1].split(" to ")[0]
        end = line.split(" to ")[1]
    elif "ABN " and "AFSL " in line:
        # using different method than the splits above
        abn_split = line.split()
        abn_value = f"{abn_split[1]} {abn_split[2]}"

    previous_line = line

# Some try/except blocks to check if the values have been found
try:
    print(f"Start: {start}\nEnd: {end}")
except NameError as e:
    print("Start/End dates not found")

try:
    print(f"ABN: {abn_value}")
except NameError as e:
    print("ABN not found")

try:
    print(f"Policy Number: {policy_number}")
except NameError as e:
    print("Policy number not found")


