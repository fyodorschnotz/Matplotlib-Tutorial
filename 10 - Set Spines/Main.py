import numpy as np
import matplotlib.pyplot as plt

sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

plt.plot(sudut,y)
plt.text(190,1,'magnituda')
plt.text(360,0.1,'sudut')

plt.xticks(np.arange(0,450,90),[r'${0}^o$',r'${90}^o$',r'${180}^o$',r'${270}^o$',r'${360}^o$'])
plt.yticks(np.arange(-1,1.5,0.5))

ax = plt.gca()
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color(('none'))
ax.spines['top'].set_color(('none'))

plt.show()