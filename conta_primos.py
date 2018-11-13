#Numero de primos

def n_primos(n):
    soma = 0
    while n > 1:
        if ePrimo(n):
            soma += 1
        n -= 1
    return soma

def ePrimo(num):
    verifica = 2
    primo = True
    while (verifica <= num) and primo:
        if (num % verifica) == 0:
            if num != verifica:
                primo = False
        verifica = verifica + 1
    return primo

#print(n_primos(5))
#print(n_primos(11))

