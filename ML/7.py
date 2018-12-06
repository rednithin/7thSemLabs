from bayespy.nodes import Dirichlet, Categorical, MultiMixture
from csv import reader
from pprint import pprint
import numpy as np

with open('7-dataset.csv') as f:
    dataset = np.array(list(reader(f)))

enum = [list(set(column)) for column in dataset.T]

dataset = np.array([[enum[i].index(j)
                     for i, j in enumerate(row)] for row in dataset])

n = len(dataset)
categoricals = []

for i in range(len(enum) - 1):
    dirichlet = Dirichlet(np.ones(len(enum[i])))
    categoricals.append(Categorical(dirichlet, plates=(n,)))
    categoricals[i].observe(dataset[:, i])

target = Dirichlet(np.ones(2), plates=tuple([len(x) for x in enum[:-1]]))
model = MultiMixture(categoricals, Categorical, target)
model.observe(dataset[:, -1])
target.update()

while True:
    tup = [enum[i].index(j)
           for i, j in enumerate(input('Tuple : ').split(','))]
    result = MultiMixture(tup, Categorical, target).get_moments()[
        0][enum[-1].index("Y")]
    print(result)
