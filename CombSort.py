# An implementation of the comb sort algorithm
# Comb sort compares elements with a certain gap between them and swaps if neccessary
# Repeat this process shrinking the gap until it is of size 1

def combSort(vector, ascending = True, k = 1.3):

	# Store the length of the vector
	n = len(vector)

	# Initialise the length of the gap between elements to be compared
	gap = n 

	# Initialise the number of swaps
	noSwaps = 0

	# Repeat until a pass with no swaps occured
	while True:

		# Reduce the gap by a factor of k
		gap = int(gap/k)

		# For every pair of elements that is a distance of k apart
		for i in range(n - gap):

			# Does a swap need to occur
			if (vector[i] > vector[i + gap] and ascending) or (vector[i] < vector[i + gap] and not ascending):
				
				# Compute the swap
				vector[i], vector[i + gap] = vector[i + gap], vector[i]
				
				# Increase the number of swaps
				noSwaps += 1

		# If no swaps occured 
		if swaps == 0:

			return vector