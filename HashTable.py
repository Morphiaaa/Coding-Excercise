class hashtable(object):
	"""docstring for hashtable"""

	def __init__(self, capacity = 1000):
		self.capacity = capacity
		self.table = [[] for i in range(capacity)]

		
	def hashFunction(self, key):
		if isinstance(key, int):
			return key % self.capacity
		elif isinstance(key, str):
			
			return sum([ord(c) for c in key]) % self.capacity
		
	def delete(self, key):
		temp_list = self.table[self.hashFunction(key)]
		for item in temp_list:
			if item[0] == key:
				temp_list.remove(item)

	def insert(self, key, value):
		return self.table[self.hashFunction(key)].append((key, value))

	def getitem(self, key):
		index = self.hashFunction(key)
		for item in self.table[index]:
			if item[0] == key:
				return item[1]
		return 'key doesn\'t exist'


h = hashtable(20)
h.insert(44, 'apple')
h.insert(92, 'banana')
h.insert(23, 'orange')
h.insert('nicole', 'beauty')
h.delete(23)
print h.getitem(23)
print h.getitem(55)
print h.getitem('nicole')

