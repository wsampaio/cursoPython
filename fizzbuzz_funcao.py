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
