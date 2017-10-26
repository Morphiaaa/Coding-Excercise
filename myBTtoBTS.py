class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

def Inorder(root, res):
	if not root:
		return 
	Inorder(root.left, res)
	res.append(root.val)
	Inorder(root.right, res)

# def CountNode(root):
# 	if not root:
# 		return 0

# 	return CountNode(root.left) + CountNode(root.right) + 1	

def ArrayToBST(array, root):
	if root is None:
		return

	Convert(array, root.left)
	root.val = array[0]
	array.pop(0)
	Convert(array, root.right)

def BTtoBST(root):
	if not root:
		return

	#n = CountNode(root)
	array = []
	Inorder(root, array)
	array.sort()
	ArrayToBST(array, root)



# def GetIndexOfRoot(root, array):
# 	counter = 1
# 	if not root:
# 		return counter

# 	stack = [root]
# 	while stack:
# 		node = stack.[]
# 		if root.right:




