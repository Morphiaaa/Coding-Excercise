import random

def randomOdd(low, high):
	if low == high:
		if low % 2 != 1:
			return 'Invalid Range'
		else:
			return low
	if low > high:
		return 'Invalid Range'

	num = random.randrange(low, high)
	return num if num % 2 == 1 else num+1


print randomOdd(3, 4)

# ask if the range is included
# corner case: low == high, low > high