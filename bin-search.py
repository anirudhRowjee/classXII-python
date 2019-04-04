# binary search

def binary_search(inlist, target):
    found = False
    ul = len(inlist) - 1
    ll = 0
    deltacounter = 0
    while not found:
        if deltacounter > len(inlist):
            print("element does not exist")
            break
        mid = (ul + ll) // 2
        mid_element = inlist[mid]
        if target > mid_element:
            ll = mid
            deltacounter += 1
        if target < mid_element:
            ul = mid
            deltacounter += 1
        elif target == mid_element:
            print(" found at ", mid)
            found = True



binary_search([1,2,3,4,5,6,7,8,9,10,11,12], 11)
