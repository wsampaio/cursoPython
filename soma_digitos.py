n = int(input("Digite um número inteiro: "))

resultado = 0

while n > 0:
    resultado = resultado + (n % 10)
    n = n // 10

print(resultado)

#o resto da divisão por 10 retorna o campo Unidade do número
#depois, uma divisão inteira por 10, não devolve o resto
#retirando então o campo Unidade
