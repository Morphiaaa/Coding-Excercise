class Node:
	"""docstring for Node"""
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None

def dfs(root, res, size):
	if root == None:
		return 0
	else:
		res.append(root.val)
	lsize = dfs(root.left, res, size)
	rsize = dfs(root.right, res, size)
	size[root] = (lsize, rsize)
	return 1 + lsize + rsize

def construct(nums, root, size):
	lsize, rsize = size[root]
	newRoot = Node(nums[lsize])
	if lsize != 0:
		newRoot.left = construct(nums[:lsize], root.left, size)
	if rsize != 0:
		newRoot.right = construct(nums[lsize + 1:], root.right, size)
	return newRoot

def convert(root):
	res = []
	size = {}
	dfs(root, res, size)
	res.sort()
	return construct(res, root, size)

def inorder(root, l):
	if root.left:
		inorder(root.left, l)
	l.append(root.val)
	if root.right:
		inorder(root.right, l)

root = Node(1)
root.right = Node(0)
# root.left = Node(2)
newRoot = convert(root)
l = []
inorder(newRoot, l)
print(newRoot.val, newRoot.left.val if newRoot.left else None, newRoot.right.val if newRoot.right else None)
print(l)
