# program to recurively find sum of first n natural number

def findsum(current, limit, sum_l):
    if current == limit :
        outstr = "sum of first " , limit, " natural numbers is ", sum_l
        print(outstr)
    else:
        sum_l += current
        current += 1
        findsum(current, limit, sum_l)


findsum(1, 2, 0)
