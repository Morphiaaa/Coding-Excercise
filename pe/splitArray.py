def splitArray(nums):
	if not nums:
		return False

	total = 0
	for i in range(len(nums)):
		total += nums[i]

	leftsum = 0
	for j in range(len(nums)-1):
		leftsum += nums[j]
		if leftsum * 2 == total:
			return True

	return False




# 	leftsum = 0

# 	for i in range(len(nums)-1):
# 		leftsum += nums[i]

# 		rightsum = 0
# 		for j in range(i+1, len(nums)):
# 			rightsum += nums[j]

# 		if leftsum == rightsum:
# 			return True


# 	return False


print splitArray([0])
