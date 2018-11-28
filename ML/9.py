import numpy as np
from random import shuffle
from csv import reader
from collections import Counter

with open('9-dataset.csv') as f:
    attrs = []
    targets = []
    dataset = list(reader(f))
    shuffle(dataset)
    for row in dataset:
        attrs.append(row[:-1])
        targets.append(row[-1])

trainLen = int(0.8 * len(dataset))
trainDataset, trainTarget = np.array(
    attrs[:trainLen], dtype='float'), targets[:trainLen]
testDataset, testTarget = np.array(
    attrs[trainLen:], dtype='float'), targets[trainLen:]

predicted = []
k = 5
for row in testDataset:
    eds = list(map(lambda x: np.sum((row - x) ** 2), trainDataset))
    kNearest = list(map(lambda x: x[1], sorted(zip(eds, trainTarget))[:k]))
    labelFreq = Counter(kNearest)
    predicted.append(labelFreq.most_common(n=1)[0][0])

correct = 0
for i, target in enumerate(testTarget):
    if predicted[i] == target:
        correct += 1

print(f"Accuracy : {correct/len(testTarget)}")
