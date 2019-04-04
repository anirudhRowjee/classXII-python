'''
PROBLEM STATEMENT
take a string of comma-separated 4-digit binary numbers and return
the numbers that are divisible by 5 as comma-separated values
'''


def return_bin_div_by_5(instr):
    l_binary = instr.split(',')
    l_binary_div_5 = [x for x in l_binary if int(x,2) % 5 == 0]
    return l_binary_div_5

z = input("enter a string of binary number separated by commas >> ")
print(return_bin_div_by_5(z))
