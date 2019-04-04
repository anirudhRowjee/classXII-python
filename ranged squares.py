'''
PROBLEM STATEMENT
generate and print a list of squares of all numbers from 1 to n 
'''

def return_squares(n):
    return([x**2 for x in range(1, n+1)])

n = int(input("enter range"))
print(return_squares(n))
