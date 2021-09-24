import csv


def load_csv_map(filename: str) -> list:
    """load a CSV file and return a list with the test order"""
    result = []
    with open(filename) as infile:
        # since the CSV file looks like a tab-delimited CSV file
        # we need to set the delimiter to '\t'
        # we also skip the first line using slicing [1:]
        # as this first line contains the column names
        # and it doesn't look like you need them
        reader = csv.reader(infile.readlines()[1:], delimiter="\t")
    for row in reader:
        # try-except block just to catch IndexError in case the file
        # contains an empty last line.
        # whether or not it does really depends on the way the CSV file is
        # generated.
        try:
            # we only need the 2nd column, based on the provided
            # information. Note the columns are zero-indexed
            result.append(row[1])
        except IndexError as e:
            # catch the IndexError to print it out, and just continue
            print(e)
            continue
    return result


def reorder_xml_file(infilename, outfilename: str, sortorder: list) -> None:
    """read xml file and reorder children based on sortorder"""
    # I'm explicitly not using and kind of XML parser as it's quite easy to
    # do the sorting with some list magic
    with open(infilename) as infile:
        inputdata = infile.readlines()

    # get indexes of the start and end of the Children element
    # put the test elements in a dict of lists for later sorting
    testelements = {}
    for index, line in enumerate(inputdata):
        if "<Children>" in line:
            childrenstartindex = index
        elif "</Children>" in line:
            childrenendindex = index
        elif "<Test Name=" in line:
            # store the element start index and name for later use
            teststartindex = index
            # element name is easy to get as it's between the 1st and
            # second " character
            elementname = line.split('"')[1]
        elif "</Test>" in line:
            # add the element to the dict as a list
            # note the + 1 offset
            testelements[elementname] = inputdata[teststartindex : index + 1]

    # start creating the output, again with the + 1 offset
    outputdata = inputdata[: childrenstartindex + 1]
    # go through the sortorder and extend the outputdata based on that
    for item in sortorder:
        outputdata.extend(testelements[item])
    # finally extend the outputdata with the last part of the input XML file
    outputdata.extend(inputdata[childrenendindex:])

    # write the now sorted file
    with open(outfilename, "w") as outfile:
        outfile.writelines(outputdata)


sortorder = load_csv_map("path/to/file/mapping.csv")
xmlinputfilename = "path/to/file/xmlinput.xml"
xmloutputfilename = "path/to/file/xmloutput.xml"

reorder_xml_file(xmlinputfilename, xmloutputfilename, sortorder)
