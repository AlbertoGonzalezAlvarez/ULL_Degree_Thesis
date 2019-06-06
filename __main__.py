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

train_data = [DataCategory.addTrainCategory(category, train_data_dict[category], ['content']) for category in train_data_dict]
test_data = [DataCategory.addTestCategory(category, test_data_dict[category], ['content']) for category in test_data_dict]

genetic_spec = SimpleGASpecification(train_data, test_data,
                                     mutation_rate = 0.7,
                                     populationSize = 20,
                                     maxIndividualFeatures = 20,
                                     fitness_penalization = 0.6,
                                     gt_max_features = 0.6,
                                     cutting_points = 15
                                     )

genetic_alg = Simple_GA(genetic_spec, generations = 50, improve = False, graphic = True)
genetic_alg.startUpGA()
#
# trained_data_dict = FileUtilities.readJSON("categories_data.json")
# categories_names = list(trained_data_dict.keys())
# categories_index = list(set(range(len(trained_data_dict))))
#
# twenty_test = fetch_20newsgroups(subset='test',
#                                  categories=categories_names, shuffle=True, random_state=42)
# docs_test = twenty_test.data
#
# text_clf = Pipeline([
#     ('vect', CountVectorizer()),
#     ('tfidf', TfidfTransformer()),
#     ('clf', MultinomialNB()),
# ])
#
# corpus_vector = [" ".join(trained_data_dict[category]) for category in categories_names]
#
# text_clf.fit(corpus_vector, categories_index)
# predicted = text_clf.predict(docs_test)
# print(metrics.classification_report(twenty_test.target, predicted,
#     target_names=twenty_test.target_names))
#
