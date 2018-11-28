from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


plt.figure(figsize=(14, 14)).subplots_adjust(hspace=0.4, wspace=0.4)
colormap = np.array(['red', 'lime', 'black'])

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

Y = pd.DataFrame(iris.target)
Y.columns = ['Targets']


def plot(i, title, targets):
    plt.subplot(2, 2, i)
    plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[targets])
    plt.title(title)
    plt.xlabel('Petal_Length')
    plt.ylabel('Petal_Width')


kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

gmm = GaussianMixture(n_components=3)
gmm.fit(X)
gmm_y = gmm.predict(X)

plot(1, 'Real', Y.Targets)
plot(2, 'K Means', kmeans.labels_)
plot(3, 'Real', Y.Targets)
plot(4, 'GMM', gmm_y)
plt.show()
