import pandas as pd

delimiter = ","
with open("69306802.csv") as infile:
    input_data = infile.read().strip("\n").split(delimiter)


df = pd.DataFrame(
    {"seconds": input_data[::3], "x": input_data[1::3], "y": input_data[2::3]}
)
print(df)
