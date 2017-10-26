def sumto3(num_list):

	left, right = 0, 0
	counter = 0

	while right < len(num_list):
		if sum(num_list[left:right+1])%3 == 0:
			counter += 1

		
