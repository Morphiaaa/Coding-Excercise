class solution:
	def __init__(self):
		self.instack = []
		self.outstack = []

	def move(self):
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())

	def push(self, num):
		self.instack.append(num)

	def pop(self):
		self.move()
		self.outstack.pop()


	def empty(self):
		return (len(self.instack) == 0) and (len(self.outstack == 0))

	def peek(self):
		self.move()
		return self.outstack[-1]


