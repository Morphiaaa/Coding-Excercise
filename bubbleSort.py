def bubblesort(stack):
	if not stack:
		return None

	for i in xrange(len(stack)):
		for j in range(1, len(stack) - i):
			if stack[j-1] > stack[j]:
				stack[j-1], stack[j] = stack[j], stack[j-1]
	return stack

stack = [9,3,2,0,6,1,5,7]
print bubblesort(stack)