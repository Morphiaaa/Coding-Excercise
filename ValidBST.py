class TreeNode:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.val = value

class BST:
	def bst(self, root, floor = float('-inf'), ceiling = float('inf')):
		if not root:
			return True

		if ceiling <= root.val and root.val <= floor:
			return False

		return self.bst(root.left, float('-inf'), root.val) and self.bst(root.right, root.val, float('inf'))

