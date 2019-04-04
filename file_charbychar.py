# read a file character by character

def read_file_by_char(path, case_count=False, letter_count=False, number_count = False, specchar_count = False):

    f = open(path, 'r+')
    if case_count:
        uppercase = 0
        lowercase = 0
    if letter_count:
        letters = 0
    if number_count:
        numbers = 0
    if specchar_count:
        spec_chars = 0
        
    while True:
        c = f.read(1)
        if c:
            if case_count:
                if c.islower(): lowercase += 1
                elif c.isupper(): uppercase += 1
                else: pass
            if letter_count:
                if c.isalpha(): letters += 1
            if number_count:
                if c.isdigit() : numbers += 1
            if specchar_count:
                if not c.isalnum() or c != ' ' : spec_chars += 1
        if not c:
            break

    print("File Statistics >>> ")
    if case_count :
        print("Uppercase letters >>> ", uppercase)
        print("Lowercase letters >>> ", lowercase)
    if letter_count:
        print("total letters >>> ", letters)
    if number_count:
        print("Numeric Characters >>> ", numbers)
    if specchar_count:
        print("Special Characters >>> ", spec_chars)

path = input("enter file path")
read_file_by_char(path, True, True, True)
