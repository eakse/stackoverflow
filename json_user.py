import json


def write_json(data, file="users.json"):
    with open(file, "w") as outfile:
        json.dump(data, outfile, indent=4)


def load_json(file="users.json"):
    # try block in case file doesn't exist
    try:
        with open(file) as infile:
            result = json.load(infile)
        return result
    except Exception as e:
        # just printing out the error
        print(e)
        # should only be file not found error
        # returning an empty dict
        return {}


while True:
    # you need to load before actually doing anything.
    # if you don't you might overwrite the file
    userlist = load_json()

    # newlines for each option
    choice = int(input("1) Register\n2) Login\n>> "))

    if choice == 1:
        username = input("Enter username: ")
        # check if user already exists before requesting password
        # since usernames are supposed to be unique, you can just 
        # create a dict with the key being username.
        # you could use the value directly for password, but
        # if you need to store more values for a user, I advice
        # you use another dict as the value.
        if username in userlist:
            print(f"User {username} already exists")
            # do some other magic here to handle this scenario
            # continue makes the while loop go to the next iteration
            continue

        password = input("Enter password: ")
        userlist[username] = {"password": password, "someotheruserdate": "dunno?"}
        write_json(userlist)

        # only print the success **after** you've actually 
        # completed all relevant logic.
        print("Registered successfully")

    # change this to elif instead of a second if statement
    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in userlist and userlist[username]["password"] == password:
            print("Logged in succesfully")
        else:
            # handle wrong username/password
            # here you need to check after getting both username&password
            print("Incorrect username/password combination")
