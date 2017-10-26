# def power_set(array):
# 	res = []
# 	if not array:
# 		return res

# 	helper(array, [], 0, res)
# 	return res

# def helper(array, path, index, res):
# 	res.append(path[:])
# 	for i in range(index, len(array)):
# 		path.append(array[i])
# 		print path
# 		helper(array, path, i+1, res)
# 		path.pop()


def power_set(array):
	res = [[]]
	for item in array:
		for ele in res[:]:
			temp = ele[:]
			temp.append(item)
			res.append(temp)
	return res

print power_set([1,2,3])
