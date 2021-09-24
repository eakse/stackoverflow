import pandas as pd
import time
import numpy as np


class bike_shop:


    bike_list = [
        {
            "ID": 1,
            "BikeName": "Bajaj CT 100",
            "Rent_hour": 139,
            "Rent_Weekly": 599,
            "Rent_Monthly": 3339
        },
        {
            "ID": 2,
            "BikeName": "Bajaj CT 100",
            "Rent_hour": 139,
            "Rent_Weekly": 599,
            "Rent_Monthly": 3339
        },
        {
            "ID": 3,
            "BikeName": "Bajaj CT 100",
            "Rent_hour": 139,
            "Rent_Weekly": 599,
            "Rent_Monthly": 3339
        },
        {
            "ID": 4,
            "BikeName": "Bajaj CT 100",
            "Rent_hour": 139,
            "Rent_Weekly": 599,
            "Rent_Monthly": 3339
        },
        {
            "ID": 5,
            "BikeName": "Bajaj CT 100",
            "Rent_hour": 139,
            "Rent_Weekly": 599,
            "Rent_Monthly": 3339
        }
    ]


    def show_catalogue(self):
        df = pd.DataFrame(bike_shop.bike_list)
        return df





class Rentshop(bike_shop):
    def __init__(self):
        self.catalogue = bike_shop.show_catalogue(self)


x = Rentshop()
print(x.catalogue)

print(x.show_catalogue())