from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import math
import pylab as pl

n = 100
x = np.linspace(0, 2 * math.pi, n)
y = np.sin(x) + 0.3 * np.random.randn(n)

neigh = KNeighborsRegressor(n_neighbors=20)
neigh.fit(x.reshape(-1, 1), y.reshape(-1, 1))
newY = neigh.predict(x.reshape(-1, 1))

pl.clf()
pl.plot(x, y, label='Noisy')
pl.plot(x, newY, label='Prediction')
pl.legend(loc='upper right')
pl.show()
