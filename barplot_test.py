import numpy as np
import matplotlib.pyplot as plt

# bar plots

x = ['IX', 'X', 'XI', 'XII']

y = [43,54,22,31]
z = [324,454,332,542]
w = np.arange(4)

plt.bar(w,y, width=0.25, color='green', label='students')
plt.bar(w+0.25,z, width=0.25, color='#0F66DD', label='marks')
plt.xticks(w,x)
plt.yticks(np.arange(0, 500, 10))
plt.legend()
plt.title('Students and marks')
plt.show()

'''
Plot a bar graph for rainfall in mm, given some zones and the months for which the rainfall is being plotted.
North Zone (jan to july) = [140, 130, 130, 190, 160, 200, 150]
South Zone (jan to july) = [160, 200, 130, 200, 200, 170, 110]
East Zone (jan to july) = [140, 180, 150, 170, 190, 140, 170]
West Zone (jan to july) = [180, 150, 200, 120, 180, 140, 110]
Central Zone (Jan to July) = [110, 160, 130, 110, 120, 170, 130]
'''


