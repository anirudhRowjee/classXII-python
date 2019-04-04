# inserting an element in a list
'''
PROGRAM LOGIC

1) append a blank element to the list
2) push all elements from required index till end to the next index
3) replace defined index with user-given number/value
'''

def insert(op_list, position, number):
    # convert position to index
    index = position - 1
    # add an empty element to the list
    op_list.append(None)
    # find number of swaps necessary, correlating with index
    # start at the second-last element (before none) and push to pos + 1
    for i in range(len(op_list)-2, index-1, -1):
        op_list[i+1] = op_list[i]
    # insert number into the list at given index
    op_list[index] = number
    return op_list
        
list_in = eval(input("enter a list"))
position = int(input("enter the position of the number you want to replace"))
number = int(input("enter value to be inserted"))

insert(list_in, position, number)

print("inserted element in list.")
print(list_in)
    
