def conver_to_number(string):
	res = 0
	for s in string:
		digit = ord(s) - ord('A') + 1
		res = 26 * res + digit
	return res

print conver_to_number('AA')

'''
start from the left, and convert letters to numbers. 
If you see more digits to the right, multiply the result you've got so far by 26, 
and use that as your initial number for your next iteration.

'''
