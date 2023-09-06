
def binary_search(array, item, begin=0, end=None):  #O(log n)
	if end is None:
		end = len(array)-1
	if begin <= end:
		m = (begin+end)//2
		if array[m] == item:
			return m
		if item < array[m]:
			binary_search(array, item,begin,m-1)
		else:
			binary_search(array, item, m+1, end)
	return None

lista = [3,4,5,6,7,3,8,90]

binary_search(lista, 6)
