import json
import functools
from operator import itemgetter, attrgetter

class Products:
    
    @staticmethod
    def sort_by_price_ascending(json_string):
        data = json.loads(json_string)
        print data
        def compare(x, y):
        	if x["price"] < y["price"]:
        		return -1
        	elif x["price"] == y["price"] and x["name"] < y["name"]:
        		return -1
        	else:
        		return 1
        #data.sort(key = functools.cmp_to_key(compare))
        #data.sort(key = itemgetter("price", "name"))
        #data.sort(key = lambda x, y: x["price"] - y["price"])
        data.sort(cmp = compare)
        return json.dumps(data)


print(Products.sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}, {"name":"apple","price":1}]'))