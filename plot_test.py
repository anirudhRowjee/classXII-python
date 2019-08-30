import numpy as np
import matplotlib.pyplot as plt


a = np.arange(1, 20, 0.5)
b = np.log(a)
c = np.cos(a)

w = np.arange(1,20, 0.5)

plt.xlabel('random values')
plt.ylabel('log / cos values')
plt.title('Log and Cos Values')
plt.xticks(w)

plt.plot(a,c, linestyle='dashdot', marker='o', label='Cos Values')
plt.plot(a,b, label='Log values')
plt.legend(loc='upper-left')
plt.savefig(fname='he2llo.pdf')
plt.show()


