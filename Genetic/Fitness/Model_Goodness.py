from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
from Genetic.Fitness import Fitness
from sklearn.metrics import f1_score
from Genetic.Components import Individual


class Model_Goodness(Fitness):

    @classmethod
    def compute(cls, individual_words: dict, test_data: dict) -> float:
        test_documents = []
        test_labels = []
        train_documents = []
        train_labels = list(range(len(individual_words)))

        for partial_individual in individual_words:
            train_documents.append(" ".join(individual_words[partial_individual]))

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

        return (sum(score_for_category)/len(individual_words))