class TreeNode:
	def __init__ (self, value):
		self.left = None
		self.right = None
		self.val = value

class Solution:
	def __init__(self, root):

		self.stack = []
		while root:
			self.stack.append(root)
			root = root.left

	def hasNext(self):
		return len(self.stack) != 0

	def next(self):
		node = self.stack.pop()
		temp = node.right
		while temp:
			self.stack.append(temp)   # update the next min value
			temp = temp.left

		return node.val


root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(25)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)

S = Solution(root)
print S.next()