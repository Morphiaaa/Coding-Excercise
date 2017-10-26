class Graph():
	'''
	1.	Assign RED color to the source vertex (putting into set U).
	2.	Color all the neighbors with BLUE color (putting into set V).
	3.	Color all neighbor’s neighbor with RED color (putting into set U).
	4.	This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2.
	5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite)
	'''
	def __init__(self, num):
		self.v = num
		self.graph = [[0 for col in range(num)] for row in range(num)]

	def isBipartite(self, start):
		colorArr = [-1] * self.v
		colorArr[start] = 1

		queue = []
		queue.append(start)
		while queue:
			u = queue.pop()

			# return False if there is a self-loop
			if self.graph[u][u] == 1:
				return False

			for v in range(self.v):
				if self.graph[u][v] == 1 and colorArr[v] == -1:
					colorArr[v] = 1 - colorArr[u]
					queue.append(v)
				elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
					return False
		return True

g = Graph(4)
g.graph = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]]

print "Yes" if g.isBipartite(0) else "No"



