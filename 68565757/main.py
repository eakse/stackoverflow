from datetime import datetime

listofnames = [
    "AG_DMW_2021052003_5150236",
    "AG_DMW_2021051903_5150236",
    "AG_DMW_2021051803_5150236",
    "AG_DMW_2021051703_5150236",
]


def get_date(string: str):
    # get the date part as a string
    spl = string.split("_")[2][0:8]
    # convert to datetime object
    return datetime.strptime(spl, "%Y%m%d")


# set initial values
last = None
today = datetime.today()
for name in listofnames:
    if last == None:
        # set the initial last
        last = name
    # you can substract dates and get the day count.
    # the one with the lowest day count is the latest
    elif (today - get_date(name)).days < (today - get_date(last)).days:
        last = name

print(last)
