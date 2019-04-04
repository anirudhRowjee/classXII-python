'''
PROBLEM STATEMENT
compute the frequency of letters in a sentence 
'''

def find_frequency(instr):
    letters = {}
    for i in instr:
        if i not in letters.keys():
            letters[i] = 1
        else:
            letters[i] = letters[i] + 1
    return letters

f = input("enter a sentence").lower()
f_frequency = find_frequency(f)
print(f_frequency)
        
