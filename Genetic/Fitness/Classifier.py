from Genetic.Fitness import *
from Genetic.Individual import *
from Genetic.Chromosome import *
from EmailParser.DataCategory import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import *
from sklearn.svm import *
from sklearn.metrics import *


class Classifier(FitnessTypes):

    @staticmethod
    def evaluate(individual: BaseIndividual, train_data: [DataCategory], weight: float, multiplier: int = 1):
        test_labels = []
        test_documents = []
        train_labels = individual.chromosome.chromosomeCategories()
        train_documents = []

        for category in train_data:
            test_labels += [category.name] * category.documents_len()

        for index in range(len(train_data)):
            test_documents += train_data[index].documents

        for category in individual.chromosome.chromosome_distribution():
            train_labels += [category] * (len(individual.chromosome.chromosome_distribution()[category]) - 1)

        for words in list(individual.chromosome.chromosome_distribution().values()):
            train_documents += words

        text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', OneVsRestClassifier(LinearSVC(class_weight="balanced")))
        ])

        # chromosome = individual.chromosome
        text_clf.fit(train_documents, train_labels)
        predicted = text_clf.predict(test_documents)

        score_for_category = precision_score(test_labels, predicted, average=None)
        individual.score += ((sum(score_for_category)) / len(individual.chromosome.chromosomeCategories())) * weight * multiplier

        # print(classification_report(test_labels, predicted, target_names=list(BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION.keys())))
        # print(confusion_matrix(test_labels, predicted))
