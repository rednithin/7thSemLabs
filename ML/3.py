import numpy as np
from csv import reader
from math import log2
from collections import Counter
from pprint import pprint

YES, NO = "Y", "N"


class Node:
    def __init__(self, label):
        self.label = label
        self.branches = {}


def entropy(data):
    total, positive, negative = len(
        data), (data[:, -1] == YES).sum(), (data[:, -1] == NO).sum()
    entropy = 0
    if positive:
        entropy -= positive / total * log2(positive / total)
    if negative:
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
    g = [gain(s, data, column) for column in range(len(data[0]) - 1)]
    return g.index(max(g))


def id3(data, labels):
    root = Node('Null')
    if entropy(data) == 0:
        root.label = data[0, -1]
    elif len(data[0]) == 1:
        root.label = Counter(data[:, -1]).most_common()[0][0]
    else:
        column = bestAttribute(data)
        root.label = labels[column]
        values = set(data[:, column])
        for value in values:
            nData = np.delete(
                data[data[:, column] == value], column, axis=1)
            nLabels = np.delete(labels, column)
            root.branches[value] = id3(nData, nLabels)
    return root


def getRules(root, rule, rules):
    if not root.branches:
        rules.append(rule[:-2] + "=> " + root.label)
    for value, nRoot in root.branches.items():
        getRules(nRoot, rule + root.label + "=" + value + " ^ ", rules)


def predict(tree, tup):
    if not tree.branches:
        return tree.label
    return predict(tree.branches[tup[tree.label]], tup)


labels = np.array(['Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis'])

with open('3-dataset.csv') as f:
    data = np.array(list(reader(f)))

tree = id3(data, labels)
rules = []
getRules(tree, "", rules)
pprint(sorted(rules))

tup = {}
for label in labels[:-1]:
    tup[label] = input(label + ": ")

print(predict(tree, tup))
