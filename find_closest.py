import pandas as pd
from datetime import date


data1 = {"Date": ["2020-01-01", "2020-01-03"],
         "ID": ["1", "2"]}
df1 = pd.DataFrame(data1)

data2 = {
    "Date": [
        '2020-01-11',
        '2020-02-03',
        '2020-04-02',
        '2020-01-05',
        '2021-01-13',
        '2021-03-03',
        '2020-01-30',
        '2020-03-31',
        '2021-04-01',
        '2021-02-02'
    ],
    "ID": [
        "11",
        "4",
        "5",
        "6",
        "1",
        "1",
        "1",
        "2",
        "2",
        "2"
    ]
}
df2 = pd.DataFrame(data2)


def get_closest_date(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    result = []
    for df1_row in df1:
        # convert df1_row['Date'] to date object
        print(df1_row)
        df1_date = date.fromisoformat(df1_row.Date)
        #reset closest
        closest = None
        for df2_row in df2:
            # check if ID matches
            if df1_row['ID'] == df2_row['ID']:
                # convert df2_row['Date'] to date object
                df2_date = date.fromisoformat(df2_row['Date'])
                # check if closest is already set, ifnot: set
                if closest == None:
                    closest = df2_date
                # else compare current closest to this row
                elif df1_date - df2_date > df1_date - closest:
                    closest = df2_date
            
        result.append(f'{closest.year}-{closest.month}-{closest.day}')
    return result


print(get_closest_date(df1, df2))