from sklearn.datasets import fetch_20newsgroups
from EmailParser import EmailEncoder, DataCategory
from Utilities import FileUtilities
from Genetic.Simple_GA_Specification import SimpleGASpecification
from Genetic.Simple_GA_Solver import Simple_GA
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics

import numpy as np

FileUtilities.startService()

if not FileUtilities.isRegistred("train_data.json", "test_data.json"):
    train_data = {
        "soc.religion.christian": fetch_20newsgroups(subset='train', remove=('quotes'), categories=['soc.religion.christian']).data,
        "talk.politics.guns": fetch_20newsgroups(subset='train', remove=('quotes'), categories=['talk.politics.guns']).data,
        "talk.politics.mideast": fetch_20newsgroups(subset='train', remove=('quotes'), categories=['talk.politics.mideast']).data
    }

    test_data = {
        "soc.religion.christian": fetch_20newsgroups(subset='test', remove=('quotes'), categories=['soc.religion.christian']).data,
        "talk.politics.guns": fetch_20newsgroups(subset='test', remove=('quotes'), categories=['talk.politics.guns']).data,
        "talk.politics.mideast": fetch_20newsgroups(subset='test', remove=('quotes'), categories=['talk.politics.mideast']).data
    }

    train_data_corpus = EmailEncoder.getCorpusFromDict(train_data)
    test_data_corpus = EmailEncoder.getCorpusFromDict(test_data)
    FileUtilities.writeToFile(train_data_corpus, "train_data.json", encoder = EmailEncoder)
    FileUtilities.writeToFile(test_data_corpus, "test_data.json", encoder = EmailEncoder)

train_data_dict = FileUtilities.readJSON("train_data.json")
test_data_dict = FileUtilities.readJSON("test_data.json")

# train_data = [DataCategory.addTrainCategory(category, train_data_dict[category], ['content']) for category in train_data_dict]
# test_data = [DataCategory.addTestCategory(category, test_data_dict[category], ['content']) for category in test_data_dict]
#
# genetic_spec = SimpleGASpecification(train_data, test_data,
#                                      mutation_rate = 0.6,
#                                      populationSize = 20,
#                                      maxIndividualFeatures = 40,
#                                      fitness_penalization = 1,
#                                      cutting_points = 7
#                                      )
#
# genetic_alg = Simple_GA(genetic_spec)
# genetic_alg.startUpGA()

trained_data_dict = FileUtilities.readJSON("categories_data.json")
categories = list(trained_data_dict.keys())
categories_index = [0, 1, 2]

twenty_test = fetch_20newsgroups(subset='test',
    categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])

corpus_vector = [" ".join(trained_data_dict[category]) for category in categories]

text_clf.fit(corpus_vector, categories_index)
predicted = text_clf.predict(docs_test)
print(metrics.classification_report(twenty_test.target, predicted,
    target_names=twenty_test.target_names))

