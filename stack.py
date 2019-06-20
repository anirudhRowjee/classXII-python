"""
STACK OPERATIONS
Main functions are -
1) pop
2) push
3) peek (check top of stack without deleting it
4) display (must check for underflow)
"""

top = None
stack = []

def show_stack(stack):
    # function to display a stack
    # input parameters are : stack (list object)
    # we set top to be a global variable (top is index of the last element)
    global top
    # check if the stack is empty
    if top is None:
        return " The stack is empty! "
    # if not, print the stack and denote top element
    else:
        for i in range(len(stack)-1, -1, -1):
            if i == top:
                print(str(stack[i]) + " <--- TOP ")
            else:
                print(stack[i])

def pop_stack(stack):
    # function to perform pop on a stack
    # input parameters are : stack (list object)
    # we set top to be a global variable (top is index of the last element)
    global top
    if top is None:
        return " Underflow: You are trying to perform operations on an empty stack! "
    else:
        # popping is removing the last element of the stack (per LIFO)
        element_to_be_popped = stack[-1]
        # we now remove the last element of the list using pop(), which is defined in python for lists
        stack.pop()
        # decrement the global top variable to signal the change in index
        if top == 0:
            top = None
        else:
            top  = top - 1
        # now that the pop is successful, we return a success message
        successmsg = " successfully popped element " + str(element_to_be_popped) + " !"
        return successmsg

def push_stack(stack, element_to_be_pushed):
    # function to push an element to as stack
    # input parameters are : stack (list object) and element_to_be_pushed (no specific type)
    # we set top to be a global variable (top is index of the last element)
    global top
    # pushing to a stack is adding an element to the end of the stack
    stack.append(element_to_be_pushed)
    # increment the global top variable to signal the change in index
    top = len(stack) - 1
    # now that the push is successful, we return a success message
    successmsg = " successfully pushed element " + str(element_to_be_pushed) + " !"
    return successmsg

def peek_stack(stack):
    # we peek a stack to view its top element without deleting it
    # we set top to be a global variable (top is index of the last element)
    global top
    # obtain the top element
    if top is None:
        return " There are no elements in this Stack! "
    else:
        # obtain element of stack with index of top
        top_element = stack[top]
        # create a message
        message = "The top element of this stack is " + str(top_element)
        # return the message
        return message

def app():
    while True:
        c = int(input("Enter the operation you want to perform : \n 1) Show the stack [1] \n 2) Peek the stack [2] \n 3) Push to the stack [3] \n 4) Pop the last element of the stack [4] \n 5) Exit [5] "))
        if c == 1 :
            show_stack(stack)
        elif c == 2:
            peek_stack(stack)
        elif c == 3:
            etbp = input("Enter element to be pushed >>> ")
            print(push_stack(stack, etbp))
            print(" Your stack currently is ")
            show_stack(stack)
        elif c == 4:
            print(pop_stack(stack))
            print(" Your stack currently is ")
            show_stack(stack)
        elif c == 5:
            print(" Thank you for using this application!")
            break

        
app()
