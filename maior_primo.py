def maior_primo(n):
    while not ePrimo(n):
        n = n - 1

    return n

def ePrimo(num):
    verifica = 2
    primo = True
    while (verifica <= num) and primo:
        if (num % verifica) == 0:
            if num != verifica:
                primo = False
        verifica = verifica + 1

    return primo


print(maior_primo(100))
print(maior_primo(50))
print(maior_primo(250))
print(maior_primo(300))

#print(ePrimo(23))
#print(ePrimo(40))


