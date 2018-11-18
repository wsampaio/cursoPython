#Maior elemento

def maior_elemento(lista):
	lst = lista[:]
	lst.sort(reverse=True)
	return lst[0]

#print(maior_elemento([3, 2, 1, 4, 6, 5, 7, 8, 9, 10, 3, 6, 9])) #Retorna 10
#print(maior_elemento([8, 14, 4, 10, 18])) #Retorna 18

