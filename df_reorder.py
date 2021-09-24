import pandas as pd


df2 = pd.read_excel(
    "path/to/file/Temperature.xlsx",
    usecols=["Station name", "Year", "Month", "Day", "Daily mean temperature"],
)
df2["Date"] = pd.to_datetime(
    {"year": df2["Year"], "month": df2["Month"], "day": df2["Day"]}
)

# get the station names
station_names = sorted([value for value in df2["Station name"].unique()])

# create the columns
columns = ["Date"]
columns.extend(station_names)

# get the dates
dates = sorted([value for value in df2["Date"].unique()], reverse=True)

# create newdf from columns
newdf = pd.DataFrame(columns=columns)

for date in dates:
    # create the newentry
    newentry = {'Date': date}
    for station in station_names:
        # find the correct 'Daily mean temperature'
        newentry[station] = df2.loc[(df2['Date'] == date) & (df2['Station name'] == station)]['Daily mean temperature']
    newdf.append(newentry)

print(newdf)