#Remove elementos repetidos

def remove_repetidos(lista):
	lista1 = sorted(lista)
	lista2 = []
	
	for i in range(len(lista1)):
		if i > 0:
			if lista1[i] != lista1[(i-1)]:
				lista2.append(lista1[i])
		else:
			lista2.append(lista1[i])

	return lista2

#lista = [3, 2, 1, 4, 6, 5, 7, 8, 9, 10, 3, 6, 9]
#lista = [8, 14, 4, 10, 18, 6, 16, 12, 20, 14, 14, 18, 16 , 8, 8]

#print(lista)
#print(remove_repetidos(lista))

