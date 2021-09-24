import pandas as pd
from pprint import pprint


data1 = {'id': ['A1234', 'A2345'],
         'Sequence': ['16 31 17', '51 59 43']}
df1 = pd.DataFrame(data1)
 

# I assumed the label en count columns are integers
data2 = {'label': [10, 11, 12, 13, 16, 17, 21, 24, 31, 43, 44, 51, 59, 60],
         'count': [214, 128, 135, 37, 184, 68, 267, 264, 231, 13, 82, 100, 99, 92]}
df2 = pd.DataFrame(data2)


def seq_value_sort(seq_df, label_df):
    new_sequence_list = []
    for value in seq_df['Sequence'].values:
        print(f'{"":-<40}') # prints a line
        # convert list of string to list of integers
        # https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
        sequence = [int(i) for i in value.split()]
        
        # generate an unsorted list of dict items based on Sequence
        data = []
        for index, row in label_df.T.iteritems():
            if int(row['label']) in sequence:
                data.append({'label': int(row['label']),
                             'count': int(row['count'])})
        pprint(data)

        # now sort the unsorted list based on key 'count'
        # https://stackoverflow.com/a/73050/9267296
        data = sorted(data, key=lambda k: k['count'])
        pprint(data)

        # list comprehension to make a sorted list oof strings
        # https://stackoverflow.com/a/7271523/9267296
        sequence_sorted = [ str(item['label']) for item in data ]
        pprint(sequence_sorted)

        # create the final sequence string from the list
        new_sequence_list.append(' '.join(sequence_sorted))
    
    # create return data
    return_data = {'id': list(seq_df['id'].values),
                   'Sequence': new_sequence_list}
    pprint(return_data)
    
    # finally return a new df
    return pd.DataFrame(return_data)


df3 = seq_value_sort(df1, df2)
print(f'{"":-<40}')
print(df3)
