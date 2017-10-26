class Minstack:
	def __init__(self):
		stack = []

	def push(self, x):
		curmin = self.getMin():
		if x < curmin or curmin == None:
			curmin = x

		stack.append([x, curmin])

	def pop(self):

		self.stack.pop()

	def top(self):
		if len(self.stack) == 0:
			return None
		else:
			self.stack[-1][0]

	def getMin(self):
		if len(self.stack) == 0:
			return None
		else:
			self.stack[-1][1]
