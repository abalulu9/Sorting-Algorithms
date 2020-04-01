# An implementation of the counting sort algorithm
# Counting sort counts the number of occurances of each distinct element
# These counts are then cycled through in ascending order of the element they represent to build the sorted vector
# Only works for integer vectors

from math import inf

def countingSort(vector, ascending= True):

	# Initialise the minimum and maximum values the vector
	maxValue = -inf 
	minValue = inf

	# Initialise the counting bins
	count = {}

	# Initialise the sorted vector
	sortedVector = []

	# For every element in the vector
	for element in vector:

		# If it's not an integer throw an exception
		if type(element) != int:
			raise Exception("All element of the vector must be an integer")

		# Try and increase the count of this element
		try:
			count[element] += 1

		# If no element of this value has been encountered set the count to 1
		except:
			count[element] = 1

		# Reassess the maximum and minimum values
		if element > maxValue:
			maxValue = element 
		if element < minValue:
			minValue = element

	# Assign the start, stop and step values
	start, stop, step = (minValue, maxValue, 1) if ascending else (maxValue, minValue, -1)

	# Cycle through the values from start to stop, in ascending or descending order
	for value in range(start, stop, step):

		# Append the number of each value counted onto the sorted vector
		try: 	
			sortedVector.extend(count[value] * [value])

		# Fails if there were no instances of the value
		except:
			pass

	return sortedVector