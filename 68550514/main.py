from urllib import parse
import json
from pprint import pprint


data_in = "%7B%22header%22%3A%22%7B%5C%22salno%5C%22%3A%5C%220%5C%22%2C%5C%22saldt%5C%22%3A%5C%22Wed+Jul+28+2021+00%3A33%3A40+GMT%2B0530+(India+Standard+Time)%5C%22%2C%5C%22soldto%5C%22%3A%5C%22%5C%22%2C%5C%22remark%5C%22%3A%5C%22%5C%22%2C%5C%22totqty%5C%22%3A310%2C%5C%22subtot%5C%22%3A20251%7D%22%2C%22details%22%3A%22%5B%7B%5C%22status%5C%22%3A%5C%22old-modified%5C%22%2C%5C%22saldtlid%5C%22%3A%5C%221%5C%22%2C%5C%22itemnm%5C%22%3A%5C%22item1%5C%22%2C%5C%22qty%5C%22%3A%5C%2218%5C%22%2C%5C%22rate%5C%22%3A%5C%2212.00%5C%22%2C%5C%22amount%5C%22%3A%5C%22216.00%5C%22%7D%2C%7B%5C%22status%5C%22%3A%5C%22new-record%5C%22%2C%5C%22saldtlid%5C%22%3A%5C%22-10%5C%22%2C%5C%22itemnm%5C%22%3A%5C%22new+item%5C%22%2C%5C%22qty%5C%22%3A%5C%2210%5C%22%2C%5C%22rate%5C%22%3A%5C%2210.00%5C%22%2C%5C%22amount%5C%22%3A%5C%22100.00%5C%22%7D%5D%22%7D"
data_out = parse.unquote(data_in)

print(type(data_out))
print(data_out)
print('----------')

data_json = json.loads(data_out)
print(type(data_json))
pprint(data_json, indent=4)
