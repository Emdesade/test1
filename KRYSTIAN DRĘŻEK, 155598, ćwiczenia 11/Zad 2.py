import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D

np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
  
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100


for c, m, zlow, zhigh in [( 'g' , 'o' , - 50 , - 25 ), ( 'b' , '^' , - 30 , - 5 ),('k','s',10 ,-33),('y','H',50 ,-3),('w','v',-10 ,44)]:
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =c, marker =m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()