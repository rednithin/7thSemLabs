from csv import reader
from pprint import pprint


def classify(hypo, row):
    for a, b in zip(hypo, row):
        if not(a == '?' or a == b):
            return 'No'
    return 'Yes'


with open("1-dataset.csv") as f:
    dataset = [row for row in reader(f)]

positive_dataset = [row[:-1] for row in dataset if row[-1] == "Yes"]
negative_dataset = [row[:-1] for row in dataset if row[-1] == "No"]
hypo_len = len(positive_dataset[0])
specific_hypothesis = positive_dataset[0][:]
generic_hypothesis = [['?'] * hypo_len]

for row in positive_dataset[1:]:
    specific_hypothesis = ["?" if tup[0] != tup[1] else tup[0]
                           for tup in zip(specific_hypothesis, row)]

for row in negative_dataset:
    newHypothesis = []
    for hypo in generic_hypothesis:
        if classify(hypo, row) == 'Yes':
            candidates = [hypo[:] for _ in range(hypo_len)]
            for i in range(hypo_len):
                if candidates[i][i] == '?':
                    candidates[i][i] = specific_hypothesis[i]
            newHypothesis += candidates
    generic_hypothesis += newHypothesis
    generic_hypothesis = list(
        filter(lambda x: True if classify(x, row) == 'No' else False, generic_hypothesis))

print(specific_hypothesis)
print(generic_hypothesis)
