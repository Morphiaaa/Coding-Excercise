def mergeStr(str_list):
	if not str_list:
		return ""


	count_list = [0] * 26

	res = ""

	for string in str_list:
		for char in string:
			if  97 <= ord(char) <= 122:
				count_list[ord(char) - 97] += 1


	start_char = 97

	for times in count_list:
		if times > 0:
			res += chr(start_char) * times
		start_char += 1

	return res


print mergeStr(['ace', 'bdf'])
print mergeStr(['greeneggs', 'ham', 'sam', 'i', 'am'])
print mergeStr([])
print mergeStr(['a','b.', 'v2@i'])
print mergeStr([""])
print mergeStr([',', '[', ']', '98'])
print mergeStr(['foobar'])
print mergeStr(['relgkhay', 'df','combojvun', 's','tpqx','ziw'])


