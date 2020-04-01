# An implementation of the quicksort algorithm
# Quicksort splits the vector around a pivot
# One vector less than, the other greater than and equal to
# Repeat the same process on all subvectors created
# Concatenate the vectors

def quickSort(vector):

	# If the vector contains 0 or 1 elements then it trivially sorted
	if len(vector) < 2:
		return vector

	# Select a pivot
	pivot = vector[0]

	# Create the two sublists
	smaller, larger = [], []

	# For each element apart from the pivot
	for element in vector[1:]:

		# Place it into the correct sublist
		if element < pivot:
			smaller.append(element)
		else:
			larger.append(element)

	# Run recursively and concatenate
	return quickSort(smaller) + [pivot] + quickSort(larger)