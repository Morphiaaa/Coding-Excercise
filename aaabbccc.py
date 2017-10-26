def compress(string):
	if len(string) == 0:
		return None

	pivot = string[0]
	count = 1
	res = ''
	for i in range(1, len(string)):
		if string[i] == pivot:
			count += 1
		else:
			temp = pivot + str(count)
			res += temp
			count = 1
			pivot = string[i]

	res += pivot + str(count)
	return res

string = 'a'
print compress(string)
