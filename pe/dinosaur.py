import csv
import heapq

class Solution(object):
	def __init__(self):
		self.heap = []
		self.dinosaur_table = dict()

	def getDinosaur(self, file):

		with open(file, 'rb') as file:

			data = csv.DictReader(file)
			for row in data:
				if row['Stance'] == '2':
					self.dinosaur_table[row['Name']] = row['feature']

	#print dinosaur_table  # this table contains all the dinosaurs whose stance is two


	def getRes(self, file):
		with open(file, 'rb') as file: 

			data = csv.DictReader(file)
			## Return a reader object which will iterate over lines in the given csvfile.
			# supports the iterator protocol and returns a dictionary each time its next() method is called
			for row in data:
				if row['Name'] in self.dinosaur_table:
					spead = self.getSpead(row['leg_length'], self.dinosaur_table[row['Name']])
					heapq.heappush(self.heap, (-spead, row['Name']))

		res = []
		while self.heap:
			res.append(heapq.heappop(self.heap)[1])
		
		with open('res.csv', 'wb') as resfile:
			reswriter = csv.writer(resfile)
			reswriter.writerow(res)

	def getSpead(self, pa1, pa2):
		return float(pa1) + float(pa2)


s = Solution()
s.getDinosaur('dataset2.csv')
s.getRes('dataset1.csv')

# data is processed in a distributed manner
# split the csv file into chunks that fit in memory size, and process the 


with open(file) as file:
	content = file.readlines()
	for line in content