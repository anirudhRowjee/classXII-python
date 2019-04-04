# multiply all numbers in a list

def multiply_all_in_list(x, product=1):
    for i in x: product *= i
    return product

l1 = eval(input('enter a list of number'))

print(multiply_all_in_list(l1))

