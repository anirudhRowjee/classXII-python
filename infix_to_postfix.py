postfix=[]
stack=[]
top=-1

def precedence(s):

    if s is '(':
        return 0
    elif s is '+' or s is '-':
        return 1
    elif s is '*' or s is'/':
        return 2
    elif s is '/':
        return 3
    else:
        return 99

infix=input("Enter: ")

for i in infix:

    if i is'(':
        stack.append(i)
        top+=1
    elif i is ')':
        next=stack.pop()
        top-=1

        while next is not '(':
            postfix.append(next)
            next=stack.pop()
            top-=1
    elif i in 'abcdefghijklmnopqrstuvwxyz':
        postfix.append(i)
        

    elif i in '+-/*^':
        p=precedence(i)

        while top>=0 and p<=precedence(stack[top]):
            postfix.append(stack.pop())
            top-=1
        stack.append(i)
        top+=1
    elif i is ' ':
        continue

while len(stack)>0:
    postfix.append(stack.pop())
    
print("It's postfix notation is: ",''.join(postfix))

























