from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from collections import Counter
import numpy as np

categories = ['alt.atheism', 'sci.med']

twenty_train = fetch_20newsgroups(subset='train',
    categories=categories, shuffle=True, random_state=42)

# count_vect = CountVectorizer()
# X_train_counts = count_vect.fit_transform(twenty_train.data)
#
# tfidf_transformer = TfidfTransformer()
# X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
#
# clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])

text_clf.fit(twenty_train.data, twenty_train.target)
print(type(twenty_train.data))
# twenty_test = fetch_20newsgroups(subset='test',
#     categories=categories, shuffle=True, random_state=42)
# docs_test = twenty_test.data
# predicted = text_clf.predict(docs_test)
# print(twenty_test.target)
# print(np.mean(predicted == twenty_test.target))