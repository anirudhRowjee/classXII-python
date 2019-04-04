# print star pattern

n = int(input('enter an odd number'))
c = input('enter character')

def starpattern(lines, character):
    if lines % 2 == 0:
        print('Even number given')
        exit()
    else:
        spaces = 2*lines - 1
        spacesstr = '{:^'+ str(spaces)+'}'
        for i in range(1, lines + 1):
            outstr = character*(2*i - 1)
            print(spacesstr.format(str(outstr)))
            
    
starpattern(n,c)
