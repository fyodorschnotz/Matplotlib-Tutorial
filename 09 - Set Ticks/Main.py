import matplotlib.pyplot as plt
import numpy as np

#membuat data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

#buat plot
plt.plot(sudut,y)
plt.ylabel('magnituda')
plt.xlabel('sudut')

jangkauanSudut = np.arange(0,450,90)

def stringSudut(): 
    for i in jangkauanSudut:
        print("r'${jangkauanSudut[i]}^o$'")

plt.yticks(np.arange(-1,2,1))
plt.xticks(jangkauanSudut,stringSudut())

#tampilkan plot
plt.show()