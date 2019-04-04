'''
PROBLEM STATEMENT
take a list as an argument and return a new list with  all the
unique elements in the first list
'''

def return_unique_elements(in_list):
    new = []
    for i in in_list:
        if i not in new : new.append(i)
        else: pass
    return new

n = eval(input("enter a python list of numbers>>> "))
print(return_unique_elements(n))



