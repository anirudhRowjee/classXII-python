'''
PROBLEM STATEMENT
generate a dictionary having keys between 1 and 20 and the values as
the square of the key
'''

def generate_dict(limit):
    dictionary = {}
    for i in range(1, limit+1):
        dictionary[i] = i**2
    return dictionary

n = int(input("enter limit"))
dictionary = generate_dict(n)
print(dictionary)
