# prime checker

def primechecker(number):
    divisors = {}
    for i in range(2, number):
        if number % i == 0:
            divisors[i] = 1
        else:
            divisors[i] = 0
    print(divisors)
    for i in divisors.values():
        if i == 1:
            print('Number is not prime')
            break
        else:
            pass
    else:
        print('Number is prime')

n = int(input('enter a number'))

primechecker(n)
