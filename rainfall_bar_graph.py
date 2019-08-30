# crucial imports
import numpy as np
import matplotlib.pyplot as plt

# rainfall trends in every region across the first seven months in a year
North = [140, 130, 130, 190, 160, 200, 150]
South = [160, 200, 130, 200, 200, 170, 110]
East = [140, 180, 150, 170, 190, 140, 170]
West = [180, 150, 200, 120, 180, 140, 110]
Central = [110, 160, 130, 110, 120, 170, 130]

# list of all the months, ticks pre-processing
months = ['january' , 'february', 'march', 'april', 'may', 'june', 'july']
w = np.arange(0,7)

# graphing rainfall across zones
plt.bar(w, North,width=0.1, color='#0d0a0b', label='North Zone Rainfall')
plt.bar(w+0.1, East, color='#454955', width=0.1, label='East Zone Rainfall')
plt.bar(w+0.2, South, color='#bce7fd', width=0.1, label='South Zone Rainfall')
plt.bar(w+0.3, West, color='#72b01d', width=0.1, label='Green Zone Rainfall')
plt.bar(w+0.4, Central, color='#3f7d20', width=0.1, label='Central Zone Rainfall')

# metadata and legends
plt.xlabel('Months')
plt.ylabel('Rainfall in mm')
plt.legend()
plt.xticks(w, months)
plt.title('Rainfall Statistics from January to July across zones')

# save the graph
plt.savefig('rainfall.pdf')

# show the figure !
plt.show()
