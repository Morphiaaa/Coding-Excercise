from collections import defaultdict
class movie(object):
	def __init__(self, name):
		self.name = name
		self.start = []

	def add_start(self, time):
		self.start.append(time)

class schedule(object):
		
	def arrange(self, movie_list):

		start_times = set()
		for movie in movie_list:
			start_times.update(movie.start)

		table = defaultdict(list)
		for time in start_times:
			for movie in movie_list:
				if time in movie.start:
					table[time].append(movie.name)

		res = set()
		self.backtracking(table, list(start_times), 0, res, '', [])
		return res

	def backtracking(self, table, start_times, index, res, path, visited):
		if index == len(start_times) and len(visited) == len(start_times):
			res.add(path)

		for i in range(index, len(start_times)):
			for name in table[start_times[i]]:
				#table[start_times[i]].remove(name)
				if name not in visited:
					self.backtracking(table, start_times, i+1, res, path + name + str(start_times[i]) + ' ', visited + [name])
				#table[start_times[i]].append(name)

if __name__ == '__main__':
	m1 = movie('baby')
	m1.add_start(14)
	m1.add_start(15)
	m1.add_start(16)
	m1.add_start(17)
	m2 = movie('driver')
	m2.add_start(14)
	m2.add_start(15)
	m2.add_start(16)
	m3 = movie('spy')
	m3.add_start(14)
	m3.add_start(15)
	m4 = movie('love')
	m4.add_start(14)
	m4.add_start(15)
	m4.add_start(17)

	sch = schedule()
	print sch.arrange([m1, m2, m3, m4])




