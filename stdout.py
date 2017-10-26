def sorted(ele, target):
	left = 0
	right = len(ele)-1

	while left < right:
		mid = (left+right+1)/2

		if ele[mid] > target:
			right = mid -1
		else:
			left = mid+1

	if ele[right] == target:
		return right

	return -1

print sorted([1,2,3,4,5], 2)