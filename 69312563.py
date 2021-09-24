from pprint import pprint

with open("packages.txt") as infile:
    data = infile.readlines()

result = []
for line in data:
    line = line.split(": ")[1]
    if ">" in line:
        line = line.split(">")[0]
    if "<" in line:
        line = line.split("<")[0]
    if " in " in line:
        line = line.split(" in ")[0]    
    result.append(line)


pprint(result[1:])

with open("69312563.txt", "w") as outfile:
    outfile.write("\n".join(result))