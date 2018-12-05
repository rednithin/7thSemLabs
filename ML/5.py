from csv import reader
from pprint import pprint
from random import shuffle, seed
from math import exp, pi, sqrt
from operator import itemgetter
import numpy as np

seed(2)
data = np.array(list(reader(open('5-dataset-alt.csv'))), dtype='float')
shuffle(data)
trainLen = int(.9 * len(data))
trainData, trainTarget = data[:trainLen, : -1], data[:trainLen, -1]
testData, testTarget = data[trainLen:, : -1], data[trainLen:, -1]


def safe_div(x, y):
    return x / y if y != 0 else 0


def getProbabilty(x, mean, std):
    exponent = exp(-safe_div((x - mean) ** 2, 2 * std ** 2))
    return safe_div(1, sqrt(2 * pi) * std) * exponent


classes = {}
for attrs, target in zip(trainData, trainTarget):
    if target not in classes:
        classes[target] = []
    classes[target].append(attrs)

summaries = {}
for cls in classes.keys():
    summaries[cls] = []
    for column in zip(*classes[cls]):
        summaries[cls].append((np.mean(column), np.std(column)))

correct = 0
for attrs, target in zip(testData, testTarget):
    probabilty = {}
    for cls in classes.keys():
        probabilty[cls] = 1
        for i, (mean, std) in enumerate(summaries[cls]):
            probabilty[cls] *= getProbabilty(attrs[i], mean, std)

    cls = sorted(probabilty.items(), key=itemgetter(1), reverse=True)[0][0]
    print(cls, target)
    if cls == target:
        correct += 1

print(f'Accuracy {correct/len(testData)}')
