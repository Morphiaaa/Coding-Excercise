	
pre = TreeNode(0)
head = pre
def doublylinkedlist(self, root):
	if not root:
		return None
	self.doublylinkedlist(root.left)
	
	root.left = pre
	pre.right = root
	pre = root

	self.doublylinkedlist(root.right)





	# start = ListNode(0)
	# cur = ListNode(0)
	# start.next = cur
	# stack = [root]

	# while stack:
	# 	node = stack.pop()
	# 	cur.pre = start
	# 	list_node = ListNode(node.val)
	# 	cur.next = ListNode(list_node)
	# 	if node.right:
	# 		stack.append(node.right)
	# 	if node.left:
	# 		stack.append(node.left)

	# 	start = cur
	# 	cur = list_node

	# return 



