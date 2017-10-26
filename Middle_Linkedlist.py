class ListNode(object):
	def __init__(self, value):
	self.next = None
	self.val = value
class Solution(object):
	def find_mid(self, head):
		if not head:
			return None

		if head.next == None:
			return head

		else:
			slow, fast = head, head
			while fast and fast.next:
				slow =slow.next
				fast = fast.next.next
			return slow
			