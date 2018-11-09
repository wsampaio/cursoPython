#Retângulos - 2

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

contaLargura = largura
contaAltura = altura

while contaAltura > 0:
    while contaLargura > 0:
        if contaAltura == altura:
            print("#", end="")
        elif contaAltura == 1:
            print("#", end="")
        elif contaLargura == largura:
            print("#", end="")
        elif contaLargura == 1:
            print("#", end="")
        else:
            print(" ", end="")

        contaLargura -= 1

    print()
    contaLargura = largura
    contaAltura -= 1



