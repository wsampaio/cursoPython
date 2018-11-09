
# n! = n . (n – 1) . (n – 2) . (n – 3)!
# ou
# 5! = 5 . 4 . 3 . 2 . 1

n = int(input("Digite o valor de n: "))

resultado = 1

while n > 0:
    resultado = resultado * n
    n = n - 1

print(resultado)