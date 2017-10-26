def move(nums):
	for i in range(len(nums)-2):
		if i == 0 and nums[0] > nums[1] and helper(nums[1:]):
			return True
		elif i == 0 and nums[0] > nums[1] and nums[0] > nums[2]:
			return False
		elif i != 0 and nums[i] > nums[i+1] and helper(nums[i+1:]) and nums[i+2] < nums[i]:
			return False
	return True

def helper(nums):
	for i in range(len(nums)-1):
		if nums[i] > nums[i+1]:
			return False
	return True

print move([3,3,2,2])
print move([4,1,2])
print move([4,3,2])