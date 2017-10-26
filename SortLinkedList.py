def sortllist(head):
	if not head:
		return None

	pre, slow , fast = head, head, head

	while fast and fast.next:
		pre = slow
		slow = slow.next
		fast = fast.next.next

	pre.next = None

	l1 = sortllist(head)
	l2 = sortllist(slow)

	dummy = ListNode(0)
	start = dummy

	while l1 and l2:
		if l1.val < l2.val:
			dummy.next = l1
			l1 = l1.next
		else:
			dummy.next = l2
			l2 = l2.next
		dummy = dummy.next

	if l1:
		dummy.next = l1

	if l2:
		dummy.next = l2

	return start.next

