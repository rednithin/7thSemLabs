import csv
import numpy as np
from random import shuffle
import math


def safe_div(x, y):
    if y == 0:
        return 0
    return x / y


def get_probability(x, mean, stddev):
    exponent = math.exp(-safe_div((x - mean) ** 2, 2 * (stddev ** 2)))
    final = safe_div(1, math.sqrt(2 * math.pi) * stddev) * exponent
    return final


data = np.array(list(csv.reader(open('5-dataset.csv'))), dtype='float')
shuffle(data)

train_length = int(0.9 * len(data))
train_data, train_target = data[:train_length, : -1], data[:train_length, -1]
test_data, test_target = data[train_length:, : -1], data[train_length:, -1]

classes = {}
for i, j in zip(train_data, train_target):
    if j not in classes:
        classes[j] = [i]
    else:
        classes[j].append(i)

summaries = {}
for i in classes:
    summaries[i] = []
    for j in zip(*classes[i]):
        summaries[i].append((np.mean(j), np.std(j)))

correct = 0
for j, k in zip(test_data, test_target):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stddev = classSummaries[i]
            x = j[i]
            probabilities[classValue] *= get_probability(x, mean, stddev)
    print(probabilities, k)

print((correct / len(test_data)) * 100)
