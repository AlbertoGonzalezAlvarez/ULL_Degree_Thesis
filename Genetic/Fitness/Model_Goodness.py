from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
from Genetic.Fitness import Fitness
from sklearn.metrics import f1_score
from Genetic.Components import Population


class Model_Goodness(Fitness):

    @classmethod
    def compute(cls, train_data: dict, test_data: dict, population: Population):
        test_documents = []
        test_labels = []
        train_documents = []
        train_labels = []

        for category_documents, index in zip(train_data.values(), range(len(train_data))):
            for documents in category_documents:
                train_documents.append(" ".join(documents))
                train_labels.append(index)

        for category_test_data, index in zip(test_data, range(len(test_data))):
            for email in category_test_data.data:
                if len(email.corpus) > 1:
                    test_documents.append(email.corpus)
                    test_labels.append(index)

        text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
        ])

        text_clf.fit(train_documents, train_labels)
        predicted = text_clf.predict(test_documents)
        score_for_category = f1_score(test_labels, predicted, average=None)

        for category, index in zip(population, range(len(population))):
            for individual in category.individuals:
                #Deshacer puntuacion global
                # individual.score = individual.score * individual.globalScore
                individual.score = (individual.score *  20 + 80 * score_for_category[index]) / 100
                # individual.globalScore = score_for_category[index]
