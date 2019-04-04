# selection sort

def selectionSort(inlist):
    # iterate through the list
    for i in range(0, len(inlist)):
        # assume that the smallest element is i
        smallest_index = i
        # iterate from i+1 to end to see if there is a smaller element
        for j in range(i+1, len(inlist)):
            if inlist[j] < inlist[smallest_index]:
                smallest_index = j
        # now smallest element fot iteration is found
        # swap ith element with the smallest element
        inlist[i], inlist[smallest_index] = inlist[smallest_index], inlist[i]
        # now, the smallest element in the iteration has been shifted to leftmost
    # return sorted list
    return inlist

inlist = eval(input("enter a list to be sorted >>> "))
sortedlist = selectionSort(inlist)
print("sorted list is ", sortedlist)
