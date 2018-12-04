from bayespy.nodes import Dirichlet, Categorical, MultiMixture
import numpy as np
from csv import reader

enum = [{'SSC': 0, 'S': 1, 'M': 2, 'Y': 3, 'T': 4}, {'M': 0, 'F': 1}, {'Y': 0, 'N': 1}, {'H': 0, 'M': 1, 'L': 2}, {
        'Athlete': 0, 'Active': 1, 'Moderate': 2, 'Sedetary': 3}, {'H': 0, 'B': 1, 'N': 2}, {'Y': 0, 'N': 1}]

data = np.array([[enum[i][j]
                  for i, j in enumerate(k)] for k in reader(open('7-dataset.csv'))])

n = len(data)

categoricals = []
for i in range(len(enum)-1):
    dirichlet = Dirichlet(np.ones(len(enum[i])))
    categoricals.append(Categorical(dirichlet, plates=(n,)))
    categoricals[i].observe(data[:, i])

target = Dirichlet(np.ones(2), plates=(5, 2, 2, 3, 4, 3))
model = MultiMixture(categoricals, Categorical, target)
model.observe(data[:, -1])
target.update()

tup = [enum[i][j] for i, j in enumerate(input('Tuple: ').split(','))]

result = MultiMixture(tup, Categorical, target).get_moments()[0][0]
print(result)
