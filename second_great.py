def getSecond(list):
	if not list:
		return None

	first, second = float('-inf'), float('-inf')

	for n in list:
		if n > first:
			second = first
			first = n
		elif second < n < first:
			second = n
	return second

print getSecond([1,2,3,4,5,6,6,7,7,8])

'''
A simple solution will be first sort the array in descending order and then return the second element from the sorted array. The time complexity of this solution is O(nlogn).

A Better Solution is to traverse the array twice. In the first traversal find the maximum element. In the second traversal find the greatest element less than the element obtained in first traversal. The time complexity of this solution is O(n).

A more Efficient Solution can be to find the second largest element in a single traversal.
'''