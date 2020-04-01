# Implementation of the insertion sorting algorithm
# Insertion sort cycles through the list element by element 
# Starting at the second element as the first is trivially sorted
# Each element is moved left until it is in the correct position
# Takes in a list of numbers and returns a sorted list

def insertionSort(vector, ascending = True):

	# For each element in the list
	for i in range(1, len(vector)):

		# Starting from the preceeding elemnent 
		# Cycle back through the elements storing the index, i.e. j
		j = i-1
		while j >= 0:

			# If (a/de)scending break when the element being check is (less/greater) than element being sorted
			if (vector[i] < vector[j] and not ascending) or (vector[i] > vector[j] and ascending):
				break

			j-=1

		# Place the element to be sorted after the breaking element
		vector.insert(j+1, vector.pop(i))

	return vector