userID = 1

print("Modify: ")
print("1. Username")
print("2. Password")
print("3. Contact number")
print("4. Location")
print()
print("Enter 'main' to back to main screen")
select = int(input()) - 1 # offset difference between selection options and 0-based list
change = input("Change to: ")

if select != 'main:':
    if select < 4 and select >=0:
        filename = f'user_{str(userID)}.txt'
        #save to individual file
        with open(filename) as infile:
            filecontents = infile.readlines()
        filecontents[select] = f'{change}\n'
        with open(filename, 'w') as outfile:
            outfile.writelines(filecontents)
        print()
        print("Changed to:", change)
        print("Change successful")
        print("\n Bring you back to <customer main menu>")
 
