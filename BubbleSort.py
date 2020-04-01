# An implementation of the bubble sort algorithm
# Bubble sort compares all adjacent pairs of elements and swaps them if neccessary 
# It repeats this until no swaps are made

def bubbleSort(vector, ascending = True):

	# Repeat until the number of swaps made in a pass is 0
	while True:

		# Initialise the number of swaps
		noSwaps = 0

		# For each adjacent pair of elements
		for i in range(len(vector) - 1):

			# If the swap needs to be made
			if (vector[i] > vector[i + 1] and ascending) or (vector[i] < vector[i + 1] and not ascending):

				# Make the swap
				vector[i], vector[i + 1] = vector[i + 1], vector[i]

				# Increase the number of swaps
				noSwaps += 1

		# If no swaps were made in this pass then return the vector
		if noSwaps == 0:
			return vector 