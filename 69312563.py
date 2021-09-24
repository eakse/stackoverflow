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


result.pop(0)
result.sort()
pprint(result)

with open("69312563.txt", "w") as outfile:
    outfile.write("\n".join(result))

string = "pyasn1, urllib3, rsa, pyasn1-modules, protobuf, idna, charset-normalizer, certifi, cachetools, six, requests, googleapis-common-protos, google-auth, pyparsing, grpcio, google-api-core, proto-plus, packaging, google-cloud-core, google-cloud-firestore"
pprint(string.split(", "))
# zip ../../../../zipped.zip cachetools certifi chardet google 