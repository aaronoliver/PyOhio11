
"""
Get data as a dict and leave it at that.

"""

import json

data = json.load(open('purses.json'))

# watch for promotional free items and signal when they're present
for purse in data['purses']:
    if not purse.get('prices'):
        print purse.get('sku'), "'IT's FREE!"
    else:
        print purse.get('price')
