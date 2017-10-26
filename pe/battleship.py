def battleship(board):
	if not board or not board[0]:
		return None


	m = len(board)
	n = len(board[0])

	for i in range(m):
		for j in range(n):
			if board[i][j] != 'X' or (i>0 and board[i-1][j] == 'X') or (j>0 and board[i][j-1] == 'X'): #not the start of the ship
				continue
			else:
				if i+2 < m and board[i+1][j] == 'X' and baord[i+2][j] == 'X':
					return [(i, j), (i+1, j), (i+2, j)]
				elif j+2 < n and board[i][j+1] == 'X' and board[i][j+2] == 'X':
					return [(i, j), (i, j+1), (i, j+2)]
					

 
