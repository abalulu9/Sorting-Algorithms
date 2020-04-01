# An implementation of the merge sorting algorithm
# Merge sort splits the vector into a set of subvectors all of length 1
# Two of the sublists are selected at random and combined them into one larger sorted list 
# This process repeats until there is only one sublist, which will be sorted

from random import shuffle

def mergeSort(vector, ascending = True):

	# Split the elements into their own lists
	sublists = [[i] for i in vector]

	# While there is more than one sublist
	while len(sublists) > 1:

		# Randomly select two lists and create a new list with their elements in order 
		shuffle(sublists)
		sublist1, sublist2 = sublists.pop(), sublists.pop()

		# Merge the two lists and add it to the set of sublists
		sublists.append(merge(sublist1, sublist2, ascending))

	return sublists[0]

def merge(vector1, vector2, ascending):

	sortedVector = []

	# While there are elements still to be sorted
	while len(vector1) + len(vector2) > 0:

		# If one vector is empty append the other vector to the sorted vector
		if len(vector1) == 0:
			sortedVector.extend(vector2)
			break
		if len(vector2) == 0:
			sortedVector.extend(vector1)
			break

		# Add the smaller of the two first elements of the vectors to the end of the sorted vector
		if (vector1[0] < vector2[0] and ascending) or (vector1[0] > vector2[0] and not ascending):
			sortedVector.append(vector1.pop(0))
		else:
			sortedVector.append(vector2.pop(0))

	return sortedVector