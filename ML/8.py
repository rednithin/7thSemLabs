import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

colormap = np.array(['red', 'lime', 'black'])

iris = load_iris()
X, Y = iris.data, iris.target


def plot(i, title, targets):
    plt.subplot(2, 2, i)
    plt.title(title)
    plt.scatter(X[:, 2], X[:, 3], c=colormap[targets])
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')


kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

gmm = GaussianMixture(n_components=3)
gmm.fit(X)
gmm_y = gmm.predict(X)

print('Kmeans: ', silhouette_score(X, kmeans.labels_))
print('GMM: ', silhouette_score(X, gmm_y))

plot(1, 'Real', Y)
plot(2, 'K Means', kmeans.labels_)
plot(3, 'Real', Y)
plot(4, 'GMM', gmm_y)
plt.show()
