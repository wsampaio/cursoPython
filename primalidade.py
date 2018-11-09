#Checagem de primos

num = int(input("Digite um número inteiro: "))

verifica = 2
primo = True

while (verifica<=num) and primo:
    if (num % verifica) == 0:
        if num != verifica:
            primo = False
    verifica = verifica + 1


if primo:
    print("primo")
else:
    print("não primo")

