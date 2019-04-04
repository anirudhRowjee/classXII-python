# program to keep record of students in bianry files
import pickle

'''
write data to binary files that maintain elementary student records
in the format [rollnumber, name, marks] in a binary file
'''

def openBinary(path):
    f = open(path, 'rb+')
    return f, path
    
def closeBinary(binfile_object):
    f.close()
    return 'success'

def readBinary(file):
    fd = pickle.load(file)
    print(fd)

p = openBinary('files/test.dat')

readBinary(p)
    
