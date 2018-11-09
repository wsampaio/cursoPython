#Exercício 5 - Verificando ordenação

a = int(input("Digite o PRIMEIRO número inteiro: "))
b = int(input("Digite o SEGUNDO número inteiro: "))
c = int(input("Digite o TERCEIRO número inteiro: "))

if b > a:
    if c > b:
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")
