'''
PROBLEM STATEMENT
take a string of hyphen separated words and return them sorted alphabetically
and separated by hyphens
'''

def bubblesort(x):
    for i in range(0, len(x)):
        for j in range(0, len(x) - i -1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

def return_sorted_string(string):
    s_list = string.split('-')
    s_list_sorted = bubblesort(s_list)
    out = ''
    for x in s_list_sorted:
        out = out + x + '-'
    return out[:-1]

z = input("enter list of words separated by hyphen >>> ")

print(return_sorted_string(z))
