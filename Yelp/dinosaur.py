import csv

with open(dataset1.csv, 'rb') as file:
	data = csv.reader(file)
	for row in data:
		print row[0]
