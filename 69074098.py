from pprint import pprint

input_string = """Payment Date: 9/14/2020 Reference: 0000232954
Invoice Number Invoice Date Voucher [ID Gross Amount Discounts Late Charges Paid Amount
102554463001 Jul/062020 21002450 699.86 0.00 0.00 699.86
112942431001 Aug/12/2020 21002565 875.96 0.00 0,00 875.96
Vendor Number Name Bank Charge Transfer Cost Cd
1000028351 OFFICE DEPOT INC $0.00
Reference Date Total Gross Amt Total Discounts Totul Late Charges Total Paid Amt

0000232954 Sep/14/2020 $1,575.82 $0.00 $0.00 $1,575.82"""

result = [[
    "Invoice Number",
    "Invoice Date",
    "Voucher ID",
    "Gross Amount",
    "Discounts",
    "Late Charges",
    "Paid Amount",
]]

for index, line in enumerate(input_string.split("\n")):
    if line.split(" ")[0] == "Invoice":
        start = index + 1
    elif line.split(" ")[0] == "Vendor":
        end = index
        break


for line in input_string.split("\n")[start:end]:
    result.append(line.split(" "))
pprint(result)


# save as CSV file:
with open('outfile.csv', 'w') as outfile:
    for row in result:
        line = 
        for column in row:
            outfile.write(f'"{column}"')