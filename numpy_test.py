import numpy as np

'''
Implementing basic features of numpy
1) create two lists having the same number of elements
'''

a = list(range(1,10))
b = list(range(11, 20))

a_np = np.array(a)
b_np = np.array(b)

c = np.array([list(range(1,6)) for x in range(6)])
d = np.array([list(range(7,12)) for x in range(6)])

print(a_np.itemsize)
print(a_np.shape)

print(a + b)
print(a_np + b_np)
print(c)
print(d)

print(c + d)


d = np.arange(10)
print(d)

print(c.itemsize)
print(c.shape)
