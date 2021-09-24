mystr = """AVP78031.1_NA   18 NLTG   0.7234     (9/9)   ++
AVP78031.1_NA   28 NYTN   0.7796     (9/9)   +++
AVP78031.1_NA   31 NSSQ   0.5689     (6/9)   +
AVP78031.1_NA   62 NVSW   0.7594     (9/9)   +++
AVP78031.1_NA  112 NTSQ   0.6953     (9/9)   ++
this_one_only_has_1_column
"""



result = []
for row in mystr.splitlines():
    columns = row.split()
    try:
        result.append([columns[0], columns[1], columns[3]])
    except IndexError as e:
        print(f'Encountered IndexError at the following row:\n{row}')
        print(f'Resulting Columns (with length: {len(columns)}):\n{columns}')

print('\nresults:')
from pprint import pprint
pprint(result)

# I think the input data might not meet your expectations, see the updated answer...