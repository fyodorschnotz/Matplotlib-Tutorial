import numpy as np
import matplotlib.pyplot as plt

"""
1. Membuat data
2. Membuat plot
3. Menampilkan plot
"""

#1(sin(2wt + theta))
#camel case
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

#2. membuat plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)

t2,y2 = sinusGenerator(1,1,4,30)
plt.plot(t2,y2, 'r')

t3,y3 = sinusGenerator(1,1,4,60)
plt.plot(t3,y3,'b--')

t4,y4 = sinusGenerator(1,1,4,90)
plt.plot(t4,y4,'y-o')

#3. menampilkan plot
plt.show()
