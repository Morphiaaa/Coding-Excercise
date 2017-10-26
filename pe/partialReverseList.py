def partialReverse(i, j, num_list):
	if i == j:
		return num_list

	# in-place
	if i > j:
		i, j = j, i

	# while i < j:
	# 	num_list[i], num_list[j] = num_list[j], num_list[i]
	# 	i += 1
	# 	j -= 1

	# return num_list



	res = num_list[:i]
	end = j

	while i <= j:
		res.append(num_list[j])
		j -= 1

	res += num_list[end+1:]

	return  res
	



print partialReverse(5,5,[1,2,3,4,5,6,7,8])


