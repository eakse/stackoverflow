import os


def autorename(filename):
    """recursive function to add " (copy)" to a filename if it already exists.
    """
    if os.path.isfile(filename):
        newfilename = f"{os.path.splitext(filename)[0]} (copy){os.path.splitext(filename)[1]}"
        return autorename(newfilename)
    else:
        return filename


print(autorename("69305596.py"))