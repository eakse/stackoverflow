import json
from pprint import pprint


def new_dict_from_template(
    storeid="",
    sellername="",
    storeurl="",
    title="",
    stock="",
    other="",
    images=[],
    req_datetime="",  # named to prevent name collision
    requestheaders="",
    responseheaders="",
) -> dict:
    return {
        "Store": [
            {
                "ID": storeid,
                "Seller": {"Name": sellername},
                "Detail": {
                    "StoreURL": storeurl,
                    "Title": title,
                    "Stock": stock,
                    "Other": other,
                    "Images": images,
                    "Request": {
                        "DateTime": req_datetime,
                        "RequestHeaders": requestheaders,
                        "ResponseHeaders": responseheaders,
                    },
                },
            }
        ],
    }


def parse(self, response):
    # Create identifying information
    record = response.url.split("/")[2] + "-" + response.url.split("/")[-2]
    record_timestamp = datetime.now().strftime("%m%d%Y%-H%M%S")
    page_filename = f"{record}-{record_timestamp}.html"
    screenshot_filename = f"{record}-{record_timestamp}.png"

    # Parse data, load to JSON object for Insert to SQL
    data_units = response.xpath("//candy-stores")
    print("Units Found: " + str(len(data_units)))

    # create a list
    not_a_json_object = []

    # Loop over each object and append to list
    for i, data_unit in enumerate(data_units):
        # not sure why you're indexing here as you don't use it in the JSON
        # you need to change the method call below
        # to match your data_unit
        not_a_json_object.append(
            new_dict_from_template(
                id="no idea",
                sellername="ABC Candy",
                other="Additional Data",
                req_datetime="12:00pm",
            )
        )


# note the [ and ] to make this a list of dicts
not_a_json_object = [new_dict_from_template()]
print(json.dumps(not_a_json_object, indent=4))
print("----------------------------------------")
not_a_json_object.append(
    new_dict_from_template(
        sellerid="no idea",
        sellername="ABC Candy",
        other="Additional Data",
        req_datetime="12:00pm",
    )
)
print(json.dumps(not_a_json_object, indent=4))
print("----------------------------------------")
# just taking one element of the list is still a valid JSON
json_str = json.dumps(not_a_json_object[1], indent=4) 
print(json_str)

with open("somejsonfile.json", 'w') as outfile:
    outfile.write(json.dumps(not_a_json_object, indent=4))