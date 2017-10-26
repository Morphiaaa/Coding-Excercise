def calculate(strlist):
	if not strlist:
		return 0

	res = []
	for fraction in strlist:
		nums = []
		temp = fraction.split('+')
		for item in temp:

			temp1 = item.split('/')
			nums.extend(temp1)

		if int(nums[1]) == 0 or int(nums[-1]) == 0:
			nn = 'divisor can not be zero'
		else:
			#print nums
			denominator = int(nums[1]) * int(nums[-1])
			numerator = int(nums[0]) * int(nums[-1]) + int(nums[1]) * int(nums[2])
			gcd = calgcd(denominator, numerator)
			while gcd != 1:
				denominator = denominator/gcd
				numerator = numerator/gcd
				gcd = calgcd(denominator, numerator)
				
			temp3 = [str(numerator), str(denominator),]
			nn = '/'.join(temp3)
			
		res.append(nn)
	return res

def calgcd(n1, n2):
	if n1 % n2 != 0:
		return calgcd(n2, n1%n2)
	else:
		return n2


list1 = ['12/2+1/3', '1/2+2/3', '0/2+2/1', '3/0+1/2']
print calculate(list1)