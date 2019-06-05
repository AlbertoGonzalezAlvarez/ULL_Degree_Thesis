from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from collections import Counter
import numpy as np
from sklearn.linear_model import SGDClassifier

categories = ['alt.atheism']

twenty_train = fetch_20newsgroups(subset='train',
    categories=categories, shuffle=True, random_state=42)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])

text_clf.fit(twenty_train.data, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test',
    categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data

predicted = text_clf.predict(docs_test)
np.mean(predicted == twenty_test.target)

# from nltk import pos_tag, word_tokenize
# from nltk.stem import WordNetLemmatizer
#
# wnl = WordNetLemmatizer()
#
#
# def penn2morphy(penntag):
#     """ Converts Penn Treebank tags to WordNet. """
#     morphy_tag = {'NN': 'n', 'JJ': 'a',
#                   'VB': 'v', 'RB': 'r'}
#     try:
#         print(morphy_tag[penntag[:2]])
#         return morphy_tag[penntag[:2]]
#     except:
#         return 'n'
#
#
# def lemmatize_sent(text):
#     # Text input is string, returns lowercased strings.
#     return [wnl.lemmatize(word.lower(), pos=penn2morphy(tag))
#             for word, tag in pos_tag(word_tokenize(text))]
#
# print(lemmatize_sent('He is walking to school with his friends'))