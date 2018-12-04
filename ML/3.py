# from sklearn.datasets import load_iris
# from sklearn import tree
# iris = load_iris()
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(iris.data, iris.target)
# print(clf.predict([[0, 0, 1, 1]]))


import numpy as np
from math import log2
from csv import reader
from pprint import pprint

YES = 'Y'
NO = 'N'


class Node:
    def __init__(self, label):
        self.label = label
        self.branches = {}


def entropy(data):
    total, posititve, negative = len(
        data), (data[:, -1] == YES).sum(), (data[:, -1] == NO).sum()
    entropy = 0
    if posititve > 0:
        entropy -= posititve / total * log2(posititve / total)
    if negative > 0:
        entropy -= negative / total * log2(negative / total)
    return entropy


def gain(s, data, column):
    values = set(data[:, column])
    gain = s
    for value in values:
        sub = data[data[:, column] == value]
        gain -= len(sub) / len(data) * entropy(sub)
    return gain


def bestAttribute(data):
    s = entropy(data)
    maxCol = -1
    maxGain = -float('inf')

    for column in range(len(data[0]) - 1):
        g = gain(s, data, column)
        if g > maxGain:
            maxGain = g
            maxCol = column

    return maxCol


def id3(data, labels):
    root = Node("NULL")

    if (entropy(data) == 0):
        if data[0, -1] == YES:
            root.label = "Yes"
        else:
            root.label = "No"
    elif len(data[0]) == 1:
        return
    else:
        column = bestAttribute(data)
        root.label = labels[column]
        values = set(data[:, column])

        for value in values:
            nData = np.delete(data[data[:, column] == value], column, axis=1)
            nLabels = np.delete(labels, column)
            root.branches[value] = id3(nData, nLabels)
    return root


def getRules(root, rule, rules):

    if not root.branches:
        rules.append(rule[:-2] + '=> ' + root.label)
    for i in root.branches:
        getRules(root.branches[i], rule + root.label + '=' + i + " ^ ", rules)


labels = np.array(['Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis'])

with open('3-dataset.csv') as f:
    data = np.array(list(reader(f)))

tree = id3(data, labels)
rules = []
getRules(tree, "", rules)
pprint(rules)
