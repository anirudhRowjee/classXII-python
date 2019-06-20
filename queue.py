"""
QUEUE OPERATIONS
1) Show queue
2) enqueue ( add to queue )
3) dequeue ( remove from queue )
"""

queue = []
front = None
rear = None

def show(queue):
    global front
    global rear
    if front is None or rear is None:
        print(" Underflow - There are no elements in the queue! ")
    else:
        for i in range(0, len(queue)):
            if i == front:
                print(queue[i] + " -- FRONT ")
            elif i == rear:
                print(queue[i] + " -- REAR ")
            else:
                print(queue[i])

def enqueue(queue, el):
    global front
    global rear
    if front is None and rear is None:
        queue.append(el)
        front = 0
        rear = 0
    else:
        queue.append(el)
        rear += 1

def dequeue(queue):
    global front
    global rear
    if front is None and rear is None:
        print("UNDERFLOW")
    elif len(queue) == 1:
        queue.pop(0)
        rear = None
        front = None
    else:
        queue.pop(0)
        rear -= 1

while True:
    print(" queue ops >> ")
    c= int(input("enter some options "))
    if c == 1:
        show(queue)
    elif c == 2:
        i = input("element to enqueue >>> ")
        enqueue(queue, i)
        show(queue)
    elif c == 3:
        dequeue(queue)
        show(queue)
        
        
    
    
