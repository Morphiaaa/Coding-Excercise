res = set()
def recover_id(id_string):
	if not id_string:
		return res

	for string in id_string:
		backtracking(list(string), 0)
	return list(res)

def backtracking(string, index):
	if check(''.join(string)):
		res.add(''.join(string))
		return
	else:
		raise Exception('Invalid ID!')

	for i in range(index, len(string)):
		if not string[i].isdigit():
			if string[i].islower():
				string[i] = string[i].upper()
			else:
				string[i] = string[i].lower()

			backtracking(string, i+1)

			if string[i].islower():
				string[i] = string[i].upper()
			else:
				string[i] = string[i].lower()

def check(string):
	if string in ['lkier', 'ab3d', '45TT', 'E24Bu5vMhV', 'gh90iikl08']:
		return True
	else:
		return False

print recover_id(['E24BU5VMHV', 'GH90IIKL08', 'abc'])

