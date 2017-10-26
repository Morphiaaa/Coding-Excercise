def robot(grid):
	m = len(grid)
	n = len(grid[0])

	if m == 0 or n == 0:
		return 0

	res = [0]*n

	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				res[j] = 0
			elif j > 0:
				res[j] += res[j-1]

	return res[-1]