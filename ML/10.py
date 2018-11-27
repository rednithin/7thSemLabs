from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import math
import pylab as pl

n = 100
x = np.linspace(0, 2 * math.pi, n)
y = np.sin(x) + 0.3 * np.random.randn(n)

neigh = KNeighborsRegressor(n_neighbors=15)
neigh.fit(x.reshape(-1, 1), y.reshape(-1, 1))

newX = np.linspace(0, 2 * math.pi, n)
newY = [neigh.predict(np.array([i]).reshape(-1, 1)) for i in newX]
newY = np.array([a[0][0] for a in newY])

print(newX, newY)
pl.clf()
pl.plot(x, y, label='Noisy')
pl.plot(newX, newY, label='Prediction')
pl.legend(loc='upper right')
pl.show()
