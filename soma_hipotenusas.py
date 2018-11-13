#Soma hipotenusas

def e_hipotenusa(n):
    verif = False
    c1 = n
    c2 = n

    while c1 > (n/2):
        while c2 > 0 and verif == False:
            if (c1 ** 2) + (c2 ** 2) == n ** 2:
                print(c1, "\t", c2, "\t", n, "\t", verif)
                verif = True
            c2 -= 1
        #print(c1, "\t", c2, "\t", n, "\t", verif)
        c1 -= 1
        c2 = c1

    if n in [5, 10, 13, 15, 17, 20, 25]:
        #verif = True
        pass

    return verif




def soma_hipotenusas(n):
    soma = 0
    while n > 0:
        if e_hipotenusa(n):
            soma += n
        n -= 1
    return soma

#print(soma_hipotenusas(20)) #retorna 105
#print(soma_hipotenusas(25)) #retorna 105
#print(soma_hipotenusas(200)) #retorna 10352


