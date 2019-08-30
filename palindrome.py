# palindrome numbers 

def is_palindrome(number):
    numstr = str(number)
    # alternate method of reversing number

    num_copy = number
    rev_numstr = ''

    while num_copy > 0:
        n = num_copy % 10
        rev_numstr += str(int(n))
        num_copy -= n
        num_copy /= 10

    if numstr == rev_numstr:
        return 'Number is a Palindrome'
    else:
        return 'Number is not a palindrome'

n = int(input("Enter a number >>> "))
print(is_palindrome(n))
