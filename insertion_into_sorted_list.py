# inserting an element into a sorted list, index finding by comparing preceding
# or succeeding elements , then inserting

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

def find_position_to_insert_to(number, inlist):
    # assume given list is sorted
    # exit cases - number to be inserted is greatet or least
    # if number is the greatest :
    if number > inlist[len(inlist) -1]:
        return 'end'
    # if number is the least
    elif number < inlist[0]:
        return 'beginning'
    # iterate through list, checking preceding/succeeding elements
    for i in range(len(inlist)-1):
        # compare elements
        if inlist[i] < number < inlist[i+1]:
            # return index of successive element to insert to
            return i + 1

def insert_into_sorted_list(op_list, number):
    # call function to find position to insert to
    position = find_position_to_insert_to(number, op_list)
    if position == 'end':
        op_list.append(number)
    elif position == 'beginning':
        insert(op_list, 1, number)
    elif type(position) is int:
        insert(op_list, position+1, number)
    else:
        return "error"
    return op_list

list_in = eval(input("enter a list"))
number = int(input("enter value to be inserted"))
print(insert_into_sorted_list(list_in, number))
        
        
    
        
