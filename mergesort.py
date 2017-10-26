class Sort:
	def mergeSort(self, array):
		if len(array) <= 1:
			return array

		mid = len(array)/2
		left = self.mergeSort(array[:mid])
		#print 'left = ' + str(left)
		right = self.mergeSort(array[mid:])
		#print 'right =' + str(right)

		return self.mergeSortedList(left, right)

	def mergeSortedList(self, list1, list2):
		res = []

		l = r = 0

		while l < len(list1) and r < len(list2):
			if list1[l] < list2[r]:
				res.append(list1[l])
				l += 1
			else:
				res.append(list2[r])
				r += 1

		if l != len(list1):
			res.extend(list1[l:])

		if r != len(list2):
			res.extend(list2[r:])

		return res

S = Sort()
stack = [0,3,-8,-32,9, 62, 33, -8, 2]
print S.mergeSort(stack)
#print stack