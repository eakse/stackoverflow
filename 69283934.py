def find_user(sheet, email):
    emails = sheet.col_values(1)
    if email in emails:
        # https://docs.gspread.org/en/latest/user-guide.html#getting-all-values-from-a-row-or-a-column
        return sheet.row_values(emails.index(email))
    else:
        return None