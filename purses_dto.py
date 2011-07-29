"""
Convert data to DTO's
"""

import json


class PurseDTO(object):
    """DTO for purse data.

    All state. No Behavior.

    """
    sku = None
    price = None
    name = None

    def __init__(self, sku, price, name):
        self.sku = sku
        self.price = price
        self.name = name


data = json.load(open('purses.json'))
for purse_data in data['purses']:
    purse = PurseDTO(purse_data['sku'], purse_data['price'], purse_data['name']) 

    if not purse.price:
        print purse.sku, "'IT's FREE!"
    else:
        print purse.price
