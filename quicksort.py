def quicksort(stack, lower, upper):
	if lower >= upper:
		return

	partition = lower  # partition refer to the last element that less than pivot in the first half list.
	for i in range(lower+1, upper+1):
		if stack[i] < stack[lower]:
			partition += 1
			stack[partition], stack[i] = stack[i], stack[partition]

	stack[partition], stack[lower] = stack[lower], stack[partition]

	quicksort(stack, lower, partition-1)
	quicksort(stack, partition+1, upper)

stack = [9, -8, 29, 4, -43, 73, 0]
quicksort(stack, 0, len(stack)-1)
print stack


