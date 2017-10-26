from operator import itemgetter, attrgetter
def sort(list):

	#return sorted(data, key=itemgetter(1))
	return sorted(list, key=lambda k: k['rating'， ‘id'])
data = [{'id':101, 'rating': 5}, {'id':1099, 'rating': 5}, {'id':102, 'rating': 5},{'id':100, 'rating': 4}, {'id':11, 'rating': 5}, {'id':1, 'rating': 4}]
print sort(data)