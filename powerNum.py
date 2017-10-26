import heapq

def getPowerNumber(index):
	pn = [pn_generator(i) for i in range(2, index + 3)]

	pn_pool = heapq.merge(*pn)

	i, last_pn = 0, 0

	while i <= index:
		power = next(pn_pool)
		if power != last_pn:
			i += 1
		last_pn = power
	return power

def pn_generator(num):
	p = 2
	while True:
		yield num ** p
		p += 1

print getPowerNumber(3)