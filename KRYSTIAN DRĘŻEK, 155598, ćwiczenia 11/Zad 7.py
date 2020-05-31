from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

np.random.seed( 444 )
fig = plt.figure()
ax = fig.gca( projection = '3d' ) 
x = np.random.sample(8)
y = np.random.sample(8)
ax.scatter(x, y, zs = 0 , zdir = 'z' ,color="r",  label = 'jabłko' )
x = np.random.sample(6)
y = np.random.sample(6)
ax.plot(x, y, zs = 0 , zdir = 'z' ,color="g" ,label = 'wąż' )
ax.legend()
ax.set_xlim( 0 , 1 )
ax.set_ylim( 0 , 1 )
ax.set_zlim( 0 , 1 )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )
ax.view_init( elev = 20. , azim =- 35 )
plt.show()