# program to write files
path_n = ''

def fileopener(path, filename, extenstion):
    file = filename + '.' + extenstion
    f = open(path+file, 'w')
    path_new = path + file
    return {'file':f, 'path':path_new}

def open_file():
    path = input("enter path >>")
    filename = input("enter filename >>")
    extension = input("enter extension >>")
    f = fileopener(path, filename, extension)['file']
    global path_n
    path_n = fileopener(path, filename, extension)['path']
    return f

def write_file(file):
    n = input("enter number of rows to write >>")
    for i in range(0, int(n)):
        p = input("enter text for row " + str(i+1))
        p = p + "\n"
        file.write(p)
    file.close()

def readfile(path, lines='all'):
    f = open(path, 'r+')
    for i in f.readlines():
        print(i[:-1])
        

f = open_file()
write_file(f)
print("path is ", path_n)
print("The lines you wrote are")
readfile(path_n)
