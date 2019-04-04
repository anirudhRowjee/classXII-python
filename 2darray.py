'''
MATRIX OPERATIONS
1) Matrix Input
2) Print matrix
3) Print diagonal of matrix
4) Print Upper and Lower halves of matrix

'''
import pprint

def populate_matrix(rows, columns, matrix):
    for i in range(0, rows):
        print('**** row ', i+1)
        row = []
        for j in range(0, columns):
            prompt = 'enter element '+ str(j+1) + ' >>>'
            row.append(int(input(prompt)))
        matrix.append(row)

def print_matrix(matrix, pretty=False):
    if not pretty:
        print ("Your Matrix Is >>>>> ")
        for i in matrix:
            print(i)
    else:
        pprint.print(matrix)

def diagonal(matrix):
    diagonal = ''
    for i in range(0, len(matrix)):
        diagonal = diagonal + str(matrix[i][i]) + ' ' 
    return diagonal

def half(matrix, param):
    
    if param == 'lower':
        print('lower half')
    if param == 'upper':
        print('upper half')
    halfmatrix = []
    length = len(matrix)
    for i in range(0, length):
        row = []
        for j in range(0, length):
            if param == 'lower':
                if i >= j:
                    row.append(matrix[i][j])
                else: row.append(' ')
            elif param == 'upper':
                if i <= j:
                    row.append(matrix[i][j])
                else: row.append(' ')
        print(row)



matrix = []
rows = int(input("enter no of rows "))
cols = int(input("enter no of columns "))

populate_matrix(rows, cols, matrix)
print_matrix(matrix)
half(matrix, 'lower')
half(matrix, 'upper')
