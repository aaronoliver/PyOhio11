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

    def __init__(self, sku, price, name=None):
        self.sku = sku
        if not price:
            raise ValueError("Price cannot be zero")
        self.price = price
        self.name = name

    def __str__(self):
        return "SECRET PURSE DATA. NO PEEKING"

    def buy_from_amazon(self, amazon_id, cc_num):
        """Lots and lots of code here
        ...
        ...
        """

data = json.load(open('purses.json'))
for purse_data in data['purses']:
    purse = PurseDTO(purse_data['sku'], purse_data['price'], purse_data['name']) 

    if not purse.price:
        print purse.sku, "'IT's FREE!"
    else:
        print purse.price
