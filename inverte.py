#Inverte sequencia

lista = []

n = int(input("Digite um número: "))

while n > 0:
	lista.append(n)
	n = int(input("Digite um número: "))

lista.sort(reverse=True)

print()
for i in lista:
	print(i)

