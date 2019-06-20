# swapping halves of a list

def swap(inlist):
    assert len(inlist)%2 == 0, "list should have even number of elements"
    delta = len(inlist) // 2
    for i in range(0, delta):
        inlist[i], inlist[i+delta] = inlist[i+delta], inlist[i]
    

l = eval(input("enter a list"))

swap(l)
print(l)
