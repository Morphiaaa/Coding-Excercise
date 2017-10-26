import sys

class Calculate(object):

	lines = sys.stdin.readlines()

	# This is a hashtable with key being the employee id and value being the employee tree node object.
	employeeTable = {}

	# This is a variable used to keep track of the next available employee id.
	nextEmployeeId = 0

	# This is used to keep track of the ceo node.
	ceoNode = None

	# This is a variable used to keep track of the company's score.
	self.res = 0


	for line in lines[1:]:
		# first, we assign the next available id to em_id.
		em_id = nextEmployeeId
		# then, we assign the score and manager_id.
		em_score, em_manager_id = line

		# find the employee tree node object.
        em_node = self.getEmployeeNode(em_id)

        # update the employee score.
        em_node.score = em_score

        # if the manager id is -1, that means current node is the ceo.
        if em_manager_id == '-1':
			ceoNode = em_node

		# we then get the manager node by passing the manager id.
		manager_node = self.getEmployeeNode(em_manager_id)

		# now we have both employee node and mananger node, we can add employee into manager's children list.
		manager_node.children.append(em_node)

		# now we update the next available by incrementing it
		nextEmployeeId +=1

	def getEmployeeNode(self, em_id):
		if em_id not in employeeTable:
			employeeTable[em_id] = TreeNode(em_id)
		return employeeTable[em_id]
		
	def calculate(self, root, parent_score):
		if root:
			self.res += min(root.score, parent_score)
			for child in root.children:
				self.calculate(child, root.score)

		
	result = self.calculate(ceoNode, None)
	sys.stdout.write(result)

 
class TreeNode(object):
	def __init__(self, eid):
		self.id = eid
		self.score = 0
		#self.parent = None
		self.children = []

