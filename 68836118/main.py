urls = [
    "https://www.allrecipes.com/recipes/416/seafood/fish/salmon/",
    "https://www.allrecipes.com/recipes/205/meat-and-poultry/pork/",
    "https://www.allrecipes.com/recipes/695/world-cuisine/asian/chinese/",
    "https://www.allrecipes.com/recipes/94/soups-stews-and-chili/",
    "https://www.allrecipes.com/recipes/qqqq/94/soups-stews-and-chili/x/y/z/q",
]

for url in urls:
    for index, part in enumerate(url.split("/")):
        if part.isnumeric():
            start = index + 1
            break
    print(url.split("/")[start:-1])


from array import *

mylist = array("i", [5, 4, 3, 2, 1, 0])


def insertionsort(mylist):
    if len(mylist) > 1:
        mylist = mylist[: len(mylist) - 1]
        insertionsort(mylist)
        i = len(mylist) - 1
        key = mylist[i]
        j = i - 1

    while j >= 0 and key < mylist[j]:
        mylist[j + 1] = mylist[j]
        j = j - 1
    mylist[j + 1] = key


insertionsort(mylist)
print(mylist)
