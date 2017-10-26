
def binary_search(nums, target):
	if not isInteger(target):
		return None

	if not nums or len(nums) == 0:
		return None

	left, right = 0, len(nums)-1

	while left <= right:
		mid = (left + right)/2
		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			left = mid +1
		else:
			right = mid - 1

	return None

[1]