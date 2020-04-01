# Implementation of the selection sorting algorithm
# Selection sort takes the smallest element of the vector, removes it and adds it to the end of the sorted vector
# Takes in a list of numbers and return a sorted list

def selectionSort(vector, ascending = True):

	sortedVector = []

	# While there are still elements in the vector
	while len(vector) > 0:

		# Find the smallest element in the vector
		index = 0
		for i in range(len(vector)):
			if (vector[i] < vector[index] and ascending) or (vector[i] > vector[index] and not ascending):
				index = i 

		# Remove the smallest element and add it to the end of the sorted vector
		sortedVector.append(vector.pop(index))		

	return sortedVector
