from __future__ import division
def sqrt(x):
	if x < 0:
		return None
	

	left = 0
	right = x

	while left <= right:
		
		mid = (left + right)//2

		if mid**2 <= x < (mid+1)**2:
			return mid
		elif x > mid**2:
			left = mid + 1
		else:
			right = mid - 1

print sqrt(17.7)