import numpy as np

'''
Implementing basic features of numpy
1) create two lists having the same number of elements
'''

a = list(range(1,10))
b = list(range(11, 20))

a_np = np.array(a)
b_np = np.array(b)

print(a_np.itemsize)
print(a_np.shape)
