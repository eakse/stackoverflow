import json
import pandas as pd


def split_data(data):
    users = []
    companies = []
    for item in data:
        for user in item["users"]:
            user["Member_No"] = item["information"]["Member_No"]
            users.append(user)
        companies.append(item["information"])
    return users, companies




with open("jsonfilegoeshere.json") as infile:
    input_data = json.load(infile)


users, companies = split_data(input_data)

users_df = pd.DataFrame(users)
companies_df = pd.DataFrame(companies)
print(users_df)
print("\n\n\n")
print(companies_df)
