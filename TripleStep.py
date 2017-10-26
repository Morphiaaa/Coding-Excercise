def steps(n):
	if n == 0:
		return 0
	res = [-1] * (n+1)
	return CountWays(n, res)

def CountWays(n, res):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	elif res[n] > -1:
		return res[n]
	else:
		res[n] = CountWays(n-1, res) + CountWays(n-2, res) + CountWays(n-3, res)
		return res[n]

print steps(90)