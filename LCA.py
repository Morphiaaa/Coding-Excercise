class TreeNode:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.val = value

class LCA:

	def lca(self, root, p, q):
		if not root:
			return None

		dict = {root: None}
		stack = [root]

		while stack:
			node = stack.pop()

			if node.left:
				parent[node.left] = node
				stack.append(node.left)

			if node.right:
				parent[node.right] = node
				stack.append(node.right)

		ancester = set()

		while p:
			ancester.add(dict[p])
			p = dict[p]

		while q not in ancester:
			q = dict[q]

		return q 

