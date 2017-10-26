def getDerangement(string):
	res = []
	if not string or len(string) == 0:
		return res

	# indexChar_map = {}
	# for i in range(len(string)):
	# 	indexChar_map[i] = string[i]

	permutation_helper(list(string), string, 0, res)
	new_res = []
	for item in res:
		temp = ''.join(item)
		new_res.append(temp)

	return new_res




'''
My idea is to generate permutations (with duplicated characters allowed), 
but while the process to check if the particular character is 
forbidden to take the particular place or not. and check if it is already been used,
we use a set to keep all the characters we used before
'''



def permutation_helper(string, original, start, result):
	#base case
	#print start
    if len(string) == start: 
    	#print start
        result.append(string[:])
        return
        
    # recursive case
    used = set()
    for i in range(start, len(original)):
        # if the element is the same as the original
        # or if the element has been used
        if string[i] == original[start] or string[i] in used:
            continue
        used.add(string[i])
        # try string[i] as the first element
        string[start], string[i] = string[i], string[start]
        permutation_helper(string, original, start+1, result)
        string[start], string[i] = string[i], string[start]
  
    return

print getDerangement('123')

# Time Comlexity: Factorial of n


