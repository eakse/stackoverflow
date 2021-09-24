import pandas as pd
import json
from pprint import pprint


with open("input_JSON.json") as infile:
    source_data = json.load(infile)
pprint(source_data)


useable_data = []
for car in source_data["car_info"]["infos"]:
    useable_data.append(car)
    useable_data[-1]["vehicle_type"] = source_data["vehicle_type"]
    useable_data[-1]["count"] = source_data["car_info"]["count"]
pprint(useable_data)


df = pd.json_normalize(useable_data)
df.to_csv("output_CSV.csv")
print(df)