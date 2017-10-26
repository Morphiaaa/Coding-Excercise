def nickname(string):
	dic = {'anna' : 'aa', 'bob' : 'bb', 'cindy': 'cy', 'david': 'dd', 'emma': 'ea', 'z' : 'zz', 'fiona': 'fa'}
	# index = 0
	# res = ''
	# while index < len(string):
	# 	start = index
	# 	while string[start: index+1] not in dic:
	# 		index += 1
	# 	#string.replace(string[start:index+1], dic[string[start:index+1]])
	# 	res += dic[string[start:index+1]]
	# 	index += 1
	# return res
	for name in dic.keys():
		if name in string:
			string = string.replace(name, dic[name])
	return string

print nickname('annabobcindyz')