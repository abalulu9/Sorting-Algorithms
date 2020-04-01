# An implementation of the shell short algorithm
# Shell sort splits the vector into subvectors
# Each subvector contains the elements that are a fixed interval apart (in terms of index)
# The subvectors are then sorted in place in the main vector
# This process repeats with the interval shrinking until it is of size 1

def shellSort(vector, ascending = True):

	# Store the length of the variable
	n = len(vector)

	# Initialise the interval
	interval = 1

	# Calculate the correct starting interval
	while interval < n / 3:
		interval = 3 * interval + 1

	# While the interval is non zero
	while interval > 0:

		# For each element that is not the first element in its subvector
		for index in range(interval, n):

			# Store the value of this element 
			element = vector[index]

			# Initialise the next index to check
			nextIndex = index - interval

			# Cycle backwards through the subvector from the element
			# Slide the elements down the subvector 
			# Insert the element in the gap after the first element less than it for ascending
			# And greater than for descending
			while nextIndex > - 1 and (vector[nextIndex] >= element and ascending or vector[nextIndex] <= element and not ascending):
				vector[nextIndex + interval] = vector[nextIndex]
				nextIndex -= interval

			# The insertion
			vector[nextIndex + interval] = element

		# Reduce the size of the interval
		interval = int((interval - 1) / 3)

	return vector