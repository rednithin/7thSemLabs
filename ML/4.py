from pprint import pprint
import numpy as np

np.random.seed(5)


def nonlin(x, deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


n_x, n_h, n_y, lRate = 2, 3, 1, 0.5

W1 = np.random.randn(n_h, n_x)
b1 = np.random.randn(n_h, 1)
W2 = np.random.randn(n_y, n_h)
b2 = np.random.randn(n_y, 1)

dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
           [3.396561688, 4.400293529, 0],
           [1.38807019, 1.850220317, 0],
           [3.06407232, 3.005305973, 0],
           [7.627531214, 2.759262235, 1],
           [5.332441248, 2.088626775, 1],
           [6.922596716, 1.77106367, 1],
           [8.675418651, -0.242068655, 1],
           [7.673756466, 3.508563011, 1]]

for epoch in range(300 + 1):
    total_error = 0
    for example in dataset:
        attrs = np.array(example[:-1]).reshape(-1, 1)
        target = example[-1]

        l0 = attrs
        l1 = nonlin(W1 @ l0 + b1)
        l2 = nonlin(W2 @ l1 + b2)

        l2_error = target - l2
        l2_delta = l2_error * nonlin(l2, deriv=True)

        l1_error = W2.T @ l2_delta
        l1_delta = l1_error * nonlin(l1, deriv=True)

        W2 += lRate * l2_delta @ l1.T
        b2 += lRate * l2_delta
        W1 += lRate * l1_delta @ l0.T
        b1 += lRate * l1_delta

        total_error += np.absolute(l2_error).sum()
    if epoch % 100 == 0:
        print(f'Epoch: {epoch} Error: {total_error}')

print('Final Weights W1 and W2')
pprint(W1)
pprint(W2)
