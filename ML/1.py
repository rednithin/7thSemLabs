from csv import reader
from pprint import pprint

f = open("1-dataset.txt", "r")
dataset = [row for row in reader(f, delimiter=",") if row[-1] == "yes"]

hypothesis = ["%"] * (len(dataset[0]) - 1)
for row in dataset:
    hypothesis = [
        "?" if tup[0] != "%" and tup[1] != tup[0] else tup[1]
        for tup in zip(hypothesis, row[:-1])
    ]

print(hypothesis)
