#Retângulos - 1

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

contaLargura = largura

while altura > 0:
    while contaLargura > 0:
        print("#", end="")
        contaLargura -= 1

    print()
    contaLargura = largura
    altura -= 1



