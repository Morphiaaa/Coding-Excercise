'''
If n = 1, there is one 1-by-1 square.

           If n = 2, there is one 2-by-2 square and four 1-by-1 squares.

           If n = 3, there is one 3-by-3 square, four 2-by-2 squares and nine 1-by-1 squares.

           If we continued the above sequence for an arbitrary n, 
           then we would have one n-by-n square, four (n - 1)-by-(n - 1) squares, 
           nine (n - 2)-by-(n - 2) squares, ... , and n2 1-by-1 squares.

           1^2 + 2^2 + 3^2 + ... + n^2
'''
def number_of_squares(n):
	if n == 0:
		return 0

	res = 0
	for i in range(1, n+1):
		res += i**2

	return res

print number_of_squares(3)
