def anagram(str1, str2):
	if not str1 and not str2:
		return 0
	#elif not str1:
	#	return len(str2)
	#else:
	#	return len(str1)

	record = {}

	for n in str1:
		if n not in record:
			record[n] = 1
		else:
			record[n] += 1

	for m in str2:
		if m in record:
			record[m] -= 1

	res = 0
	for value in record.values():
		if value > 0:
			res += value

	return res


def getMinDiff(a, b):
	res = []

	for i in range(len(a)):
		if len(a[i]) != len(b[i]):
			res.append(-1)
		else:
			res.append(anagram(a[i], b[i]))
	return res

print getMinDiff(['aba', 'bbvd', 'e'], ['aaa', 'ieop', 'i'])