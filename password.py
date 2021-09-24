from pprint import pprint


def process_two_lines(line1: str, line2: str) -> dict:
    # determine which of the 2 variables is the password and which is the username
    if 'password' in line1.split('-')[0]:
        passwordline = line1
        userline = line2
    else:
        passwordline = line2
        userline = line1
    
    # the join is needed in case the password contains a "-" character
    password = '-'.join(passwordline.split('-')[1:]).strip('\n') 
    username = '-'.join(userline.split('-')[1:]).strip('\n')
    service = userline.split('username')[0]
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


logininfo = get_login_info('test1.txt')
pprint(logininfo)
print('----------\n\n')

for index, line in enumerate(logininfo):
    print(f'{index:2}: {line["service"]}')

service = int(input('Please select the service for which you want the username/password:\n'))
print(f'Username:\n{logininfo[service]["username"]}\nPassword:\n{logininfo[service]["password"]}\n')