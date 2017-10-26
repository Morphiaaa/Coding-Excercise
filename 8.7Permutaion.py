def permutaion(string):
	res = []
	if not string:
		return res

	helper(list(string), list(string), 0, res)
	return res

def helper(string, path, start, res):
	if len(path) == start + 1:
		res.append(path[:])
		return

	for i in range(start, len(string)):
		path[i], path[start] = path[start], path[i]
		helper(string, path, start+1, res)
		path[i], path[start] = path[start], path[i]

	return 

print permutaion('abc')