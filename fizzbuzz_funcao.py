#FizzBuzz

def fizzbuzz(n):
    if n % 3 == 0:
        if n % 5 == 0:
            return "FizzBuzz"
        else:
            return "Fizz"
    else:
        if n % 5 == 0:
            return "Buzz"
        else:
            return n

#print(fizzbuzz(3)) #deve devolver Fizz
#print(fizzbuzz(6)) #deve devolver Fizz
#print(fizzbuzz(12)) #deve devolver Fizz
#print(fizzbuzz(93)) #deve devolver Fizz
#print(fizzbuzz(5)) #deve devolver Buzz
#print(fizzbuzz(15)) #deve devolver FizzBuzz
#print(fizzbuzz(4)) #deve devolver 4

#O resultado dos testes com seu programa foi:

#***** [0.25 pontos]: Checando se Fizz é identificado corretamente (3) - Falhou *****
#***** [0.25 pontos]: Checando se Fizz é identificado corretamente (6) - Falhou *****
#***** [0.25 pontos]: Checando se Fizz é identificado corretamente (12) - Falhou *****
#***** [0.25 pontos]: Checando se Fizz é identificado corretamente (93) - Falhou *****
#***** [0.25 pontos]: Checando se Buzz é identificado corretamente (5) - Falhou *****
#***** [0.25 pontos]: Checando se Buzz é identificado corretamente (20) - Falhou *****
#***** [0.25 pontos]: Checando se Buzz é identificado corretamente (230) - Falhou *****
#***** [0.25 pontos]: Checando se Buzz é identificado corretamente (12355) - Falhou ****
#***** [0.25 pontos]: Checando se FizzBuzz é identificado corretamente (15) 
