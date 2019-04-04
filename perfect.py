# perfect number

def is_perfect(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    sum_div = 0
    for x in divisors : sum_div += x
    if sum_div == number:
        return number, ' is a Perfect Number'
    else:
        return number, ' is not a perfect number'

x = int(input('enter a number >>> '))

print(is_perfect(x))
