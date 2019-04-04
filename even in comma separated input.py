'''
PROBLEM STATEMENT
take a comma-separated input from a user, return all even numbers in a tuple
'''

def return_even_tuple(list_in_str):
    list_in = l.split(',')
    list_in = [int(x) for x in list_in]
    even_list = [x for x in list_in if x % 2 == 0]
    out = ()
    for x in even_list: out = out + (x,)
    return out

l = input("enter a comma separated list of numbers >>> ")

print(return_even_tuple(l))
