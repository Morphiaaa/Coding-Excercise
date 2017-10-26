class Node:
	def __init__(self, value):
		self.next = None
		self.val = value

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, data):
		node = Node(data)
		node.next = self.head
		self.head = node


	def printlist(self, llist):
		temp = llist
		while temp:
			print temp.val
			temp = temp.next


	def addtwonumber(self, l1, l2):
		res = Node(0)
		head = res
		carry = 0

		while l1 or l2 or carry:
			n1 = n2 = 0
			if l1:
				n1 = l1.val
				l1 = l1.next
			if l2:
				n2 = l2.val
				l2 = l2.next

			sum = n1 + n2 + carry
			digit = sum%10
			carry = sum/10

			res.next = Node(digit)
			res = res.next

		return res.next

llist1 = LinkedList()
llist1.push(9)
llist1.push(1)
llist1.push(3)

llist2 = LinkedList()
llist2.push(2)
llist2.push(3)
llist2.push(5)

print llist1.addtwonumber(llist1.head, llist2.head)