
def busca(lista, elem):
	for i in range(len(lista)):  #O(n)
		if lista[i] == elem:
			return i
	return None

lista = ["python","pokemon",45,6,7]
elemento = "pokemon"

indici = busca(lista,elemento)

if indici:
	print(f"O índici do elemento {elemento} é: {indici}")
else:
	print(f"O elemento {elemento} não se encontra na lista")

