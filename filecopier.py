# file copier
def copy_file(path_to_source, path_to_copy):
    source = open(path_to_source, 'r')
    copy = open(path_to_copy, 'w')

    lines = source.read()
    copy.write(lines)

    source.close()
    copy.close()

    print("finished copying")

source = input("enter path to source >>>")
copy = input("enter path to copy >>>")
copy_file(source, copy)
                
