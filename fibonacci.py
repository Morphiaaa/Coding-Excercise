
dic = {0: 0, 1: 1}
def fibonacci(n):
	# if n not in dic:
	# 	dic[n] = fibonacci(n-1) + fibonacci(n-2)
	# return dic[n]

	# Recursion, exponential time, T(n) = T(n-1) + T(n-2)
	# Extra Space: O(n) if we consider the function call stack size, otherwise O(1).
	# if n == 0:
	# 	return 0
	# elif n == 1:
	# 	return 1
	# else:
	# 	return fibonacci(n-1) + fibonacci(n-2)


	# Dynamic programming  O(n)time O(n)space
	# f = [0] * (n+1)
	# f[1] = 1
	# for i in range(2, n+1):
	# 	f[i] = f[i-1] + f[i-2]
	# return f[n]


	# O(n), O(1)
	a, b = 0, 1
	while n > 0:
		a, b = b, a+b
		n -= 1
	return a

print fibonacci(5)