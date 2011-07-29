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

    def __init__(self, sku, price=None, name=None):
        self.sku = sku
        self.price = price or 0 # assume free if no price given
        self.name = name


data = json.load(open('purses.json'))
for purse_data in data['purses']:
    purse = PurseDTO(purse_data['sku'], purse_data.get('price'), purse_data['name']) 

    if not purse.price:
        print purse.sku, "'IT's FREE!"
    else:
        print purse.price
