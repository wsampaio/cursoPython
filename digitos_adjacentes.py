# verifique se o número recebido possui ao 
# menos um dígito com um dígito adjacente igual a ele.
# Ex: 3556

n = int(input("Digite um número inteiro: ")) 

possui = False 
verifica = 0 

while n > 0: 
    verifica = n % 10 
    n = n // 10 
    if (n % 10) == verifica: 
        possui = True 


if possui: 
    print("sim") 
else: 
    print("não") 
