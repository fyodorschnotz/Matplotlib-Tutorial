import numpy as np
import matplotlib.pyplot as plt

"""
1. Membuat data
2. Membuat plot
3. Menampilkan plot
"""

#membuat data
x = np.arange(1,6,1)
y = x**2
y2 = y**2
#membuat plot
plt.plot(x,y)
plt.plot(x,y2)

#menampilkan plot
plt.show()

