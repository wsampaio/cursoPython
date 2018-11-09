n = int(input("Digite o valor de n: "))
resultado = 0

while n > 0:
    resultado = resultado + 1
    if resultado % 2 != 0:
        print(resultado)
        n = n - 1

