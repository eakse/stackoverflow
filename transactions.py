import gspread
import pandas as pd


# set variables
docid = '1sLXgSfpdD0o_4ulUc6rDCOq_YSyHek-xJLR_cvQfy6Q'
worksheetid = 'transactions'
credfile = 'path/to/file/credentials.json'
csvfile = 'path/to/file/transactions.csv'


# load GSheet
gc = gspread.service_account(filename=credfile)
sheet = gc.open_by_key(docid)
worksheet = sheet.worksheet(worksheetid)


# load CSV file into df
df_csv = pd.read_csv(csvfile)


def method1(worksheet: gspread.Worksheet, df: pd.DataFrame):
    """This is the 'cheaty' way. Just load the existing worksheet, 
    append df and overwrite existing worksheet.
    Note that this doesn't check if the values in df are already
    in the worksheet...

    Args:
        worksheet (gspread.Worksheet): the worksheet with which to work
        df (pd.DataFrame): the df to append
    """
    # just load existing GSheet into a df
    df_cheat = pd.DataFrame(worksheet.get_all_records())
    # perform append. You might want to play with how you merge/append
    # This method has the advantage of easy sorting.
    df_cheat = df_cheat.append(df).sort_values(by='Date')
    # overwrite worksheet
    # you could easily create a new worksheet with this method as you have
    # the df_cheat to work with
    worksheet.update([df_cheat.columns.values.tolist()] + df_cheat.values.tolist())


def method2(worksheet: gspread.Worksheet, df: pd.DataFrame):
    """This method goes through the df row by row and adds
    it to the worksheet by using casting.
    https://www.w3schools.com/python/python_casting.asp

    Args:
        worksheet (gspread.Worksheet): the worksheet with which to work
        df (pd.DataFrame): the df to append
    """
    # go over the values in the df by row
    for row in df.values:
        # cast as list
        row = list(row)
        # if you leave out the table_range it will append at the end
        worksheet.append_row(row)


method1(worksheet, df_csv)
method2(worksheet, df_csv)


# updatesheet.append_row([update], table_range='A1')


# update = latest[latest['Date'] > max_date] 
# # latest data in a df to insert 
# updatesheet = sheet.worksheet("testpy") 
# # test sheet to inset into 
# set_with_dataframe(updatesheet, update, include_column_header=False) 
