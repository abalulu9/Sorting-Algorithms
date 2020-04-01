# An implementation of the heapsorting algorithm
# Heapsort first turns the vector into a heap
# It then swaps the first and last elements of the unsorted heap
# This puts the largest unsorted element of the heap at the end of the vector
# Reheap the unsorted elements and repeat the swap process

def buildHeap(vector):

	# Store the length of the vector
	n = len(vector)

	# Cycle back through the vector creating the heap
	for i in range(n, -1, -1):
		vector = heapify(vector, i, n)

	return vector

def heapSort(vector):

	# Build the heap
	vector = buildHeap(vector)
	
	# Working backward through the heap, row by row
	for i in range(len(vector)-1, 0, -1):

		# Swap the root vertex and the current vertex
		vector[i], vector[0] = vector[0], vector[i]
		
		# Rebuild the heap with the unsorted elements
		vector = heapify(vector, 0, i)

	return vector

def heapify(vector, i, n):

	# Set indicies for the parent and two children vertices
	parent = i 
	left = 2 * i + 1
	right = 2 * i + 2

	# For each child nodes
	for child in [left, right]:

		# If the child exists
		# And if it is the largest of the trio checked so far
		if child < n and vector[child] > vector[parent]:

			# The variable parent represents the new parent of the next iteration
			# If the variable remains unchanged, this branch is heaped successfully
			parent = child 

	# If the element is no longer the parent, swap the element and the new parent
	if parent != i:
		vector[i], vector[parent] = vector[parent], vector[i]

		# Continue down the rest of the branch
		vector = heapify(vector, parent, n)

	return vector