from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from pprint import pprint

categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']

train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

c, t = CountVectorizer(), TfidfTransformer()

train_tr = t.fit_transform(c.fit_transform(train.data))

model = MultinomialNB()
model.fit(train_tr, train.target)

test_tr = t.transform(c.transform(test.data))
predicted = model.predict(test_tr)

print("Accuracy:", accuracy_score(test.target, predicted))

print("Classification Report:")
print(classification_report(test.target, predicted, target_names=test.target_names))

print("Confusion Matrix:")
pprint(confusion_matrix(test.target, predicted))
