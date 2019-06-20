# matrix addition

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

def populate_matrices_in_list(matrices, force_rows, force_cols):
    counter = 1
    for matrix in matrices:
        print(" >>>>>>> matrix ", counter)
        populate_matrix(force_rows, force_cols, matrix)
        counter += 1

def add_matrices_in_list(matrices, force_rows, force_cols):
    endmatrix = []
    for i in range(0, force_rows):
        r = []
        for j in range(0, force_cols):
            r.append(0)
        endmatrix.append(r)
    
    for matrix in matrices:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows != force_rows or cols != force_cols :
            print("unequal matrices")
        else:
            for i in range(0, rows):
                for j in range(0, cols):
                    endmatrix[i][j] += matrix[i][j]
    return endmatrix
        
def subtract_matrices_in_list(matrices, force_rows, force_cols):

    endmatrix = matrices[0]
    
    for matrix in matrices[1:]:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows != force_rows or cols != force_cols :
            print("unequal matrices")
        else:
            for i in range(0, rows):
                for j in range(0, cols):
                    endmatrix[i][j] -= matrix[i][j]
    return endmatrix

def multiply_2_matrices(matrix1, matrix2, new):
    # check if matrices can be multiplied
    assert len(matrix1) == len(matrix2[0]), "matrices cannot be multiplied"
    # begin iteration
    
                       

matrix1 = []
matrix2 = []
matrixlist = [matrix1, matrix2]
rows = 2
cols = 2
populate_matrices_in_list(matrixlist, rows, cols)

# addition & subtraction block

'''
added = add_matrices_in_list(matrixlist, rows, cols)
subtracted = subtract_matrices_in_list(matrixlist, rows, cols)
print(" added ")
print_matrix(added)
print(" subtracted ")
print_matrix(subtracted)
'''

# multiplication block


multiplied = []

d
