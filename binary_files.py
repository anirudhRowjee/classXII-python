# write records to a binary file 
import pickle

# function to create a binary file
def create_bin_file(name, path):
    name = name+'.dat'
    filepath = path + name
    f = open(filepath, 'wb+')
    return {'file':f, 'path':filepath}

#function to write a given number of lines to a binary file
def write_bin_file(path, no_of_lines):
    file = open(path, 'wb+')
    for i in range(1, no_of_lines+1):
        instr = "enter line no " + str(i) + " to write >>> "
        line = input(instr)
        pickle.dump(line, file)
        print("wrote line '", line, "' to file ")
    print("****Finished writing operation****")


# function to read binary files line by line
def read_bin_files(path, no_of_lines):
    file = open(path, 'rb+')
    lines = pickle.load(file)
    file.seek(0)
    for i in range(0, no_of_lines):
        line = pickle.load(file)
        print("line ", i , " >>> ", line)

'''
RUNTIME
'''

# take file name and path as creation arguments
name = input("enter binary file name >> ")
path = input("enter file path (with trailing slash) >>")

# call creation function
file_actual = create_bin_file(name, path)

# save file object, path as global variables
path_created = file_actual['path']
file_created = file_actual['file']

# show that file has been created at the location specified
print('**** created file ', file_created , ' at ', path_created)
file_created.close()
          
# writing to a binary file
nl = int(input("enter number of lines to write to file >>> "))
write_bin_file(path_created, nl)

# reading lines from a binary file
path_created = 'files/test.dat'
print("**** reading binary file at ", path_created)
read_bin_files(path_created, nl)

