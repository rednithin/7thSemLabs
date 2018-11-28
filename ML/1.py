from csv import reader
from pprint import pprint

with open("1-dataset.csv") as f:
    dataset = [row[:-1] for row in reader(f) if row[-1] == "yes"]

hypothesis = dataset[0][:]
for row in dataset[1:]:
    hypothesis = ["?" if tup[0] != tup[1] else tup[0]
                  for tup in zip(hypothesis, row[:-1])]
print(hypothesis)
