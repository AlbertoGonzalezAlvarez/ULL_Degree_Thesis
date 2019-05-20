# from sklearn.datasets import fetch_20newsgroups
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import Pipeline
# from collections import Counter
# import numpy as np
# from sklearn.metrics import f1_score
#
# categories = ['alt.atheism']
# categoriesa = ['alt.atheism', 'talk.politics.mideast']
#
# twenty_train = fetch_20newsgroups(subset='train',
#     categories=categories, shuffle=True, random_state=42)
#
# # count_vect = CountVectorizer()
# # X_train_counts = count_vect.fit_transform(twenty_train.data)
# #
# # tfidf_transformer = TfidfTransformer()
# # X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
# #
# # clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
#
# text_clf = Pipeline([
#     ('vect', CountVectorizer(vocabulary=['religion', 'guns', 'police'])),
#     ('tfidf', TfidfTransformer()),
#     ('clf', MultinomialNB()),
# ])
#
# # print(twenty_train.target) # Categoria a la que pertenece, cada categoria se reperesenta con un numero
# # print(twenty_train.data[0]) #Cada uno de los documentos (correos).
#
# text_clf.fit(twenty_train.data, twenty_train.target)
# # print(type(twenty_train.data))
# twenty_test = fetch_20newsgroups(subset='test',
#     categories=categoriesa, shuffle=True, random_state=42)
# docs_test = twenty_test.data
# predicted = text_clf.predict(docs_test)
# # print(twenty_test.target)
# score = f1_score(twenty_test.target, predicted, average=None)
#
# print(score)

from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names()

for col in set(X.nonzero()[1]):
    print(feature_names[col], ' - ', X[0, col])