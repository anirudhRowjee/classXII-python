# recursive binary search

'''
PROGRAM LOGIC ->>

1) take in a sorted list
2) establish the start point and end point of the list as upper and lower bounds
3) find the middle element within the bounds
4) if the target element is greater than the middle, move search to right and change the bounds (upper bound stays the same, lower bound becomes the middle element)
5) if the target element is lower than the middle, move to the left and change the bounds (lower bound stays the same, upper bound becomes the middle element)
6) if the the target element is the middle element, then it is found (print index and found message)


RECURSIVE FUNCTION LOGIC ->>

1) parameters - list, upper bound, lower bound, target, iteration(delta)
2) exit condition - if the middle element is the target element, the process exits
    or
    if the delta count is greater than the length of the list
    or
    if upper or lower limit elements are target
3) recursive call conditions - middle element is not the target element
    If middle element is lower, call the function again with the changed bounds, delta ++
    If middle element is higher, call the function with changed bounds, delta ++
4) element not found - if delta is greater than the length of the list, exit

'''

def binsearch(inlist, target, upper, lower, delta=0):
    
    # finding middle element
    mid  = (upper + lower)//2
    # find upper bound element
    upper_element  = inlist[upper]
    #find lower bound element
    lower_element = inlist[lower]
    
    # assign middle element to variable
    mid_element = inlist[mid]
    
    # check for exit condition one - delta > length of list
    if delta >= len(inlist):
        print("element does not exist")
    
    # check for exit condition two - middle element is the target element (with elif so it does not execute if exit condition 1 is fulfilled)
    elif target == mid_element:
        success = "TARGET ELEMENT ", target, " FOUND AT ", mid
        print(success)

    # check for exit condition three - upper/lower bound element is target

    # if target is upper element
    elif target == upper_element:
        print("FOUND AT ", upper)

    # if target is lower element
    elif target == lower_element:
        print("FOUND AT ", lower)
    

    # if all exit conditions fail, move to recursive part
    else:
        # check if target is lesser than middle element
        if target < mid_element:
            # change upper bound to be middle element
            upper = mid
            # add delta 
            delta += 1
            # call function again
            binsearch(inlist, target, upper, lower, delta)
            
        # check if target is greater than middle element
        elif target > mid_element:
            # change lower bound to be middle element
            lower = mid
            # add delta 
            delta += 1
            # call function again
            binsearch(inlist, target, upper, lower, delta)

binsearch([1,2,3,4,5,6,7,8,9,10], 9, 8, 0)
