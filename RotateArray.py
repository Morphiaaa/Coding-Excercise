class Solution:
	def findValue(self, array, target):
		if not array:
			return None

		left, right = 0, len(array)-1

		while left <= right:
			mid = (left + right) / 2
			if array[mid] == target:
				return True
			while left < right and array[mid] == array[left]:
				left += 1
			if array[mid] <= array[right]:
				if array[mid] < target <= array[right]:
					left = mid + 1
				else:
					right = mid - 1
			else:
				if array[left] <= target < array[mid]:
					right = mid -1
				else:
					left = mid + 1
		return False


S = Solution()
array = [1,0,0,0,0,1,1,1]
print S.findValue(array, 1)

