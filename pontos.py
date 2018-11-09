import math

#Distância entre dois pontos

#print("Vamos descobrir a distância entre dois pontos")
#print()

distancia = 0
ax = int(input("Digite o valor Ax: "))
ay = int(input("Digite o valor Ay: "))
bx = int(input("Digite o valor Bx: "))
by = int(input("Digite o valor By: "))


if ax == bx:
    distancia = ay-by
elif ay == by:
    distancia = ax-bx
else:
    # d = (a² + b²) sqrt(2)
    distancia = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

if distancia < 0:
    distancia = distancia * -1



#print(distancia)

if distancia < 10:
    print("perto")
else:
    print("longe")







