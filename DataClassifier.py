# from Utilities import FileUtilities
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import Pipeline
# from sklearn import metrics
#
#
# class DataClassifier:
#
#     @classmethod
#     def results(cls, fields: list):
#         trained_data_dict = FileUtilities.readJSON("categories_data.json")
#         test_data_dict = FileUtilities.readJSON("test_data.json")
#
#         categories_names = list(trained_data_dict.keys())
#         categories_index = list(set(range(len(trained_data_dict))))
#
#         text_clf = Pipeline([
#             ('vect', CountVectorizer()),
#             ('tfidf', TfidfTransformer()),
#             ('clf', MultinomialNB()),
#         ])
#
#         data_corpus_vector = [" ".join(trained_data_dict[category]) for category in trained_data_dict]
#         test_corpus_vector = []
#         test_labels = []
#
#         for category, index in zip(categories_names, range(len(test_data_dict))):
#             for field in fields:
#                 test_corpus_vector.append(" ".join(test_data_dict[category]))
#                 test_labels.append(index)
#
#         text_clf.fit(data_corpus_vector, categories_index)
#         predicted = text_clf.predict(test_corpus_vector)
#         print(metrics.classification_report(test_labels, predicted,
#                                             target_names=categories_names))