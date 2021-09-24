from pprint import pprint


def process_two_lines(line1: str, line2: str) -> dict:
    # determine which of the 2 variables is the password and which is the username
    if 'password' in line1.split('-')[0]:
        passwordline = line1
        userline = line2
    else:
        passwordline = line2
        userline = line1

    password = passwordline.split('-')[1].strip('\n') # gets the part after the - separator, removing the newline
    username = userline.split('-')[1].strip('\n') # gets the part after the - separator, removing the newline
    service = userline.split('username')[0] # gets the service part
    return {
        'username': username,
        'password': password,
        'service':  service
    }    



def get_login_info(filename: str) -> dict:
    # read file
    with open(filename) as infile:
        filecontents = infile.readlines()
    
    result = []
    # go through lines by pair
    for index, line1 in enumerate(filecontents[::2]):
        result.append(process_two_lines(line1, filecontents[(index*2)+1]))

    return result

pprint(get_login_info('test1.txt'))
