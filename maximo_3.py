#Maximo com 3 parametros

def maximo(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

#print(maximo(30, 14, 10)) #deve devolver 30
#print(maximo(0, -1, 1)) #deve devolver 1

