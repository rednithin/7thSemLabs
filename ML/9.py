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

k = 5
correct = 0
for row, target in zip(testDataset, testTarget):
    eds = [np.sum((row - x) ** 2) for x in trainDataset]
    kNearest = np.array(sorted(zip(eds, trainTarget))[:k])[:, -1]
    predicted = Counter(kNearest).most_common()[0][0]

    print(f'Actual: {target.ljust(15)} \t\tPredicted: {predicted}')
    if predicted == target:
        correct += 1

print(f"Accuracy : {correct/len(testTarget)}")
