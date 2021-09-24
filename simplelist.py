from pprint import pprint

animals = """Name: Dave
Species: Dog
Size: Big
Food: Meat
Observation: Dave like to eat food because
he likes it very much.

Name: Mitchel
Species: Mouse
Size: Big
Food: Cheese
Observation: Mitchel likes cheese.

Name: Tommy
Species: Bird
Size: Small
Food: Seeds
Observation: He does not like corn."""





def processtxt(current_animal):
    # CSV don't like commas in their strings as this messes up the structure
    # You can be safe by enclosing values in ""
    animal = [
        f'''"{current_animal[0].strip('Name: ')}"''',
        f'''"{current_animal[1].strip('Species: ')}"''',
        f'''"{current_animal[2].strip('Size: ')}"''',
        f'''"{current_animal[3].strip('Food: ')}"''',
        f'''"{current_animal[4].strip('Observation: ')}'''
    ]
    # check if there are multiple observation lines
    print(animal[-1])
    if len(current_animal) > 4:
        animal[4] += ''.join(current_animal[5:])
    # add the closing "
    animal[4] += '"'
    # return the results as a CSV line
    return ','.join(animal)


csv_list = []
current_animal = []
# split by end of line
for line in animals.splitlines():
    # check if we're done with the animal
    # by checking for the empty line
    if line.strip() == '':
        # transform the current_animal into CSV line
        csv_list.append(processtxt(current_animal))
        # reset the current_animal
        current_animal = []
    else:
        print(line)
        current_animal.append(line)

# check if there's still a current_animal pending
if len(current_animal) > 0:
    csv_list.append(processtxt(current_animal))


with open('animals.csv', 'w') as outfile:
    for line in csv_list:
        outfile.write(f'{line}\n')

