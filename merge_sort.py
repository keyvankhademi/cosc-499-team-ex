from heapq import merge

def merge_sort(arr):

	N = len(arr)
	if N <= 1:
		return arr

	# Recursively sort the array
	L = merge_sort(arr[:N//2])
	R = merge_sort(arr[N//2:])

	return list(merge(L, R))
