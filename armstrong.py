# armstrong numbers

def is_armstrong(number):
    number_copy = number
    digits = 0
    digit_list = []
    answer = 0

    # finding number of digits
    while number_copy > 0:
        n = number_copy % 10
        digit_list.append(n)
        digits += 1
        number_copy //= 10

    #adding all digits to check if armstrong number
    for i in digit_list:
        answer += i**digits
        
    if answer == number:
        return str(number) + ' is an armstrong number'
    else:
        return str(number)+ ' is not an armstrong number'


number = int(input('enter a number >>> '))

print(is_armstrong(number))
