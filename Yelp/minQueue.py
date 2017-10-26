from collections import deque
class MinQueue(object):
	def __init__(self):
		self.queue = deque()
		self.values = [] # ascending order

	def push(self, x):
		self.queue.append(x)
		if len(self.values) == 0:
			self.values.append(x)
		else:
			left = 0
			right = len(self.values)-1
			while left <= right:
				mid = (left+right)//2
				
				if self.values[mid] < x:
					left = mid + 1
				else:
					right = mid -1
			self.values = self.values[:left] + [x] + self.values[left:]


	def popleft(self):
		popNum = self.queue.popleft()
		if popNum == self.values[0]:
			self.values.remove(popNum)

		return popNum

	def getMin(self):
		if self.values:
			return self.values[0]
		else:
			return None


if __name__ == '__main__':
	mq = MinQueue()
	mq.push(1)
	print mq.popleft()
	print mq.getMin()