'''
PROBLEM STATEMENT :
Take a string as a parameter. Calculate the number of
uppercase and lowercase letters.
'''

def letter_case_counter(string):
    uppercase_range = range(65, 91)
    lowercase_range = range(97, 123)
    uppercase_letters = 0
    lowercase_letters = 0
    for i in string:
        if ord(i) in uppercase_range:
            uppercase_letters += 1
        elif ord(i) in lowercase_range:
            lowercase_letters += 1
        else:
            pass
    return {'uppercase':uppercase_letters, 'lowercase':lowercase_letters}

s = input('enter a string')

letters = letter_case_counter(s)
print("Lowercase letters = ", letters['lowercase'])
print("Uppercase letters = ", letters['uppercase']) 
