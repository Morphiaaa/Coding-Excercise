def countHoles(num):
	res = 0
	if num == 0:
		return 1
	while num != 0:
		n = num % 10
		if n in [4,6,9,0]:
			res += 1
		elif n == 8:
			res += 2

		num = num/10

	return res

print countHoles(8801)


