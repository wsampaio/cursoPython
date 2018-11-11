#FizzBuzz

def fizzbuzz(n):
    if (n % 3 == 0) and (n % 5 != 0):
        return "Fizz"
    elif (n % 3 != 0) and (n % 5 == 0):
        return "Buzz"
    elif (n % 3 == 0) and (n % 5 == 0):
        return "FizzBuzz"
    else:
        return n

#print(fizzbuzz(3)) #deve devolver Fizz
#print(fizzbuzz(5)) #deve devolver Buzz
#print(fizzbuzz(15)) #deve devolver FizzBuzz
#print(fizzbuzz(4)) #deve devolver 4
