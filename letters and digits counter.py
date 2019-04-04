'''
PROBLEM STATEMENT
take a sentence and return the number of letters, digits
'''

def find_letter_digit_count(x):
    lettercount = 0
    digitcount = 0
    for character in x:
        if character.isalpha(): lettercount+=1
        elif character.isdigit(): digitcount+=1
        else: pass
    return {'letters':lettercount, 'digits':digitcount}

s = input("Enter an alphanumeric sentence").lower()

counts = find_letter_digit_count(s)

print("Letters >>> ", counts['letters'])
print("Digits >>> ", counts['digits'])
