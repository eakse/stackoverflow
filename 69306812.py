results = []
for j in search(userquery, tld="com", num=amt, stop=amt, pause=0): 
    print(j) 
    results.append(str(j))

with open("filename_goes_here.txt", "w") as outfile:
    outfile.writelines(results)