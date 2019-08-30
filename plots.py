# plots
import matplotlib.pyplot as plt
import numpy as np

x = ['VIII', 'IX', 'X', 'XI', 'XII']
y = [45, 32, 30, 30, 28]

plt.xlabel = "Classes"
plt.ylabel = "Students"
plt.title("Some Stuff")


plt.plot(x,y, linestyle='solid', linewidth=2, color='#FF0000', marker='s', markeredgecolor='#000000', markersize=10)
plt.show()






