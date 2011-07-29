"""
Use namedtuple's
"""

import json
from collections import namedtuple

Purse = namedtuple('Purse', 'sku name price')

data = json.load(open('purses.json'))
purses = [Purse(**p) for p in data['purses']]

for purse in purses:
    if not purse.price:
        print purse.sku, "'IT's FREE!"
    else:
        print purse.price
