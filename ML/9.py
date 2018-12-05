import numpy as np
from random import shuffle, seed
from csv import reader
from collections import Counter

seed(4)

with open('9-dataset.csv') as f:
    dataset = np.array(list(reader(f)))
    shuffle(dataset)

trainLen = int(0.8 * len(dataset))
trainDataset, trainTarget = np.array(
    dataset[:trainLen, :-1], dtype='float'), dataset[:trainLen, -1]
testDataset, testTarget = np.array(
    dataset[trainLen:, :-1], dtype='float'), dataset[trainLen:, -1]

predicted = []
k = 5
for row in testDataset:
    eds = list(map(lambda x: np.sum((row - x) ** 2), trainDataset))
    kNearest = np.array(sorted(zip(eds, trainTarget))[:k])[:, -1]
    labelFreq = Counter(kNearest)
    predicted.append(labelFreq.most_common(n=1)[0][0])

correct = 0
for i, target in enumerate(testTarget):
    print(f'Actual: {target.ljust(15)} \t\tPredicted: {predicted[i]}')
    if predicted[i] == target:
        correct += 1

print(f"Accuracy : {correct/len(testTarget)}")
