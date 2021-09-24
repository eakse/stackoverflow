from pprint import pprint



with open('ftldata2.xml') as infile:
    data = infile.readlines()


bplist = []
weaponlist = set()
for line in data:
    if '<blueprintList' in line:
        bplist.append(line.split('"')[1])

    if 'shipBlueprint' in line:
        break
    if '<name>' in line:
        name = line.split('<name>')[1].split('<')[0]
        if not (
            'FIGHTER' in name or
            'BOMBER' in name or
            'TROOPSHIP' in name or
            'SCOUT' in name or
            'MINER' in name or
            'FREIGHTER' in name or
            'FIRESHIP' in name or
            'TRUFFLE' in name or
            'CROISSANT' in name or
            'JELLY_BUTTON' in name or
            'REBEL_FAT' in name or
            'REBEL_SKINNY' in name or
            'ROCK_FIGHT' in name or
            'ROCK_ASSAULT' in name or
            'AUTO_ASSAULT' in name or
            'AUTO_BASIC' in name or
            'HUNTER' in name
        ):
            weaponlist.add(name)

# pprint(bplist)
with open('ftl-out.txt', 'w') as outfile:
    for line in sorted(weaponlist):
        outfile.write(f'{line}\n')
pprint(weaponlist)