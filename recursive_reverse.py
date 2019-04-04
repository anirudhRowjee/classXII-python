# recrusively reversing a string

def find_last_char(input_string, final_string):
    # take a working string (input_string) and the reversed string (final_string)
    if len(input_string) == 1:
        # if there is only one charater left, add the last character an print the string
        final_string += input_string
        print (" reversed string is >>> ", final_string)
    else:
        # find the last character of the string
        char_tba = input_string[-1]
        # modify the input string to exclude last character
        input_string = input_string[:-1]
        # modify final string to add last character
        final_string = final_string + char_tba
        # call the function again
        find_last_char(input_string, final_string)

rev = input("please enter a string to be reversed >>> ")
find_last_char(rev, '')
