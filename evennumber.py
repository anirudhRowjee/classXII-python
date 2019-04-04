'''
PROBLEM STATEMENT
take a list and return a new list with all the even values from the first
'''

def return_even(in_list):
    return([x for x in in_list if x % 2 == 0])

n = eval(input("Enter a list of numbers >>> "))
print(return_even(n))
