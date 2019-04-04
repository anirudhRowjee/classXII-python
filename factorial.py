# compute the factorial of a number



def factorial(number):
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    return factorial

number  = int(input('enter a number >>> '))
print('The factorial of ' + str(number) + ' is ' + str(factorial(number)))
    
