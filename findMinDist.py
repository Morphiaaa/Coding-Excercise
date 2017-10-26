from collections import deque
def findMinDist(v ,u, n, edges):
	visited = [False]
	queue = deque()
	distance = [0] * n

	queue.append(u)
	visited[u] = True

	while queue:
		vertice = queue.popleft()

		for i in range(len(edges[vertice])):
			if edges[vertice][i] not in visited:
				distance[edges[vertice][i]] = distance[vertice]+1
				visited[edges[vertice[i]]] = True
				queue.append(edges[vertice][i])


	return distance[v]

def addEdge(edges, u, v):
	edges[u].append(v)
	edges[v].append(u)



	
