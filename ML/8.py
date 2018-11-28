import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


plt.figure(figsize=(14, 14)).subplots_adjust(hspace=0.4, wspace=0.4)
colormap = np.array(['red', 'lime', 'black'])

iris = load_iris()
X, Y = iris.data, iris.target


def plot(i, title, targets):
    plt.subplot(2, 2, i)
    plt.scatter(X[:, 2], X[:, 3], c=colormap[targets])
    plt.title(title)
    plt.xlabel('Petal_Length')
    plt.ylabel('Petal_Width')


kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

gmm = GaussianMixture(n_components=3)
gmm.fit(X)
gmm_y = gmm.predict(X)

plot(1, 'Real', Y)
plot(2, 'K Means', kmeans.labels_)
plot(3, 'Real', Y)
plot(4, 'GMM', gmm_y)
plt.show()
