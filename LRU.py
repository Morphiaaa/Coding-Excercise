class Node:
	def __init__(self, key, value):
		self.key = key
		self.val = value
		self.next = None
		self.pre = None

class LRUcache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.dict = dict()
		self.head = Node(0, 0)
		self.tail = Node(0, 0)
		self.head.next = self.tail
		self.tail.pre = self.head

	def get(self, key):
		if key in self.dict:
			self.remove(self.dict[key])
			self.add(self.dict[key])
			return self.dict[key]
		return -1

	def put(self, key, value):
		if key in self.dict:
			self.remove(self.dict[key])

		node = Node(key, value)
		self.add(node)
		self.dict[key] = node

		if len(self.dict) > capacity:
			n = self.head.next
			self.remove(n)
			del self.dict[n.key]


	def remove(self, node):
		p = node.pre
		n = node.next
		p.next = n
		n.pre = p

	def add(self, node):
		p = self.tail.pre
		p.next = node
		node.pre = p
		node.next = self.tail
		self.tail.pre = node