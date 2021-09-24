from pprint import pprint
import requests
from pandas import json_normalize
import json
import pandas as pd
import numpy as np
from pprint import pprint
# try this

total_df = pd.DataFrame()

with open("69306432.json") as infile:
    data = json.load(infile)
df = json_normalize(data)

item_list = df["dataset"]
current_df = pd.DataFrame()


for i in item_list:
    pprint(i)
    current_df.loc[0, "y"] = i[0]["data"][0]["y"]
    try:
        pass
    except Exception as e:
        print(e)
        current_df.loc[0, "y"] = np.nan
    try:
        current_df.loc[0, "meas"] = i[0]["meas"]
    except Exception as e:
        print(e)
        current_df.loc[0, "meas"] = np.nan
    try:
        current_df.loc[0, "label"] = i[0]["label"]
    except Exception as e:
        print(e)
        current_df.loc[0, "label"] = np.nan

total_df = pd.concat([total_df, current_df])


total_df.to_excel("C:/Users/svetl/Onedrive/Desktop/work/output.xlsx", index=False)
