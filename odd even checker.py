# odd_even_checker

def odd_even_checker(*numbers):
    # iterate through the list of numbers
    for i in numbers:
        #check if the type is integer
        try:
            i + 1
        except TypeError:
            pass
        # return appropriate answer 
        if i % 2 == 0:
            out = 'number ' + str(i) + ' is even'
            return(out)
        else:
            out = 'number ' + str(i) + ' is odd'
            return(out)
        

z = int(input('enter a number >>> '))
print(odd_even_checker(z))
