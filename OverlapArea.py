def countstep(steps):
	if not steps:
		return 0

	x, y = map(int, steps[0].split())

	for step in steps[1:]:
		newx, newy = map(int, step.split())
		if newx > 0:
			x = min(x, newx)
		if newy > 0:
			y = min(y, newy)

	return x*y	