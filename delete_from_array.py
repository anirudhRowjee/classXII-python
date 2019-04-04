# deletion from an array in place

def get_pos(element, inlist):
    for i in range(0 , len(inlist)):
        if inlist[i] == element:
            return i
    else:
        return -1

def compress(index, inlist):
    #print(inlist)
    inlist[index] = None
    #print(inlist)
    # start swapping from index tbd to end, so null element is in end
    for i in range(index, len(inlist)-1):
        inlist[i], inlist[i+1] = inlist[i+1], inlist[i]
    #print(inlist)
    return inlist[:-1]

def delete_element(element, inlist):
    element_tbd_index = get_pos(element, inlist)
    if element_tbd_index == -1:
        return "element does not exist"
    else:
        return compress(element_tbd_index, inlist)

inlist = eval(input("enter a list >>> "))
e_tbd = int(input("enter element to be deleted "))

print(delete_element(e_tbd, inlist))
