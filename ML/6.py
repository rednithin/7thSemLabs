from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']

train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

c, t = CountVectorizer(), TfidfTransformer()

trainTr = t.fit_transform(c.fit_transform(train.data))
testTr = t.transform(c.transform(test.data))

model = MultinomialNB()
model.fit(trainTr, train.target)
predicted = model.predict(testTr)

print('Accuracy : ', accuracy_score(test.target, predicted), sep='\n')
print('Classification Report : ', classification_report(
    test.target, predicted, target_names=test.target_names), sep='\n')
print('Confusion Matrix : ', confusion_matrix(test.target, predicted), sep='\n')
