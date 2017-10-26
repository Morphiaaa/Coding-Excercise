def multiply(num1, num2):
	smaller = num1 if num1 < num2 else num2
	bigger = num2 if num1 < num2 else num1
	res = helper(smaller, bigger)
	return res

# def helper(smaller, bigger):
# 	if smaller == 0:
# 		return 0
# 	elif smaller == 1:
# 		return bigger

# 	half = smaller >> 1
# 	side1 = helper(half, bigger)

# 	if smaller % 2 == 0:
# 		return side1 + side1
# 	else:
# 		return side1 + side1 + bigger


def helper(smaller, bigger):
	c = 1
	sub = smaller
	res = 0
	while bigger >= smaller:
		if bigger >= sub:
			bigger -= sub
			res += c
			sub << 1
			c << 1
		else:
			sub >> 1
			c >> 1

	return res

print multiply(15, 5)