from EmailParser import EmailEncoder, DataCategory
from Utilities import FileUtilities
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfTransformer
from Genetic import *

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

train_data = [DataCategory.addTrainCategory(category, train_data_dict[category], ['msg']) for category in train_data_dict]
test_data = [DataCategory.addTestCategory(category, test_data_dict[category], ['msg']) for category in test_data_dict]

problem_spec: GeneticAlgorithmSpecification = GeneticAlgorithmSpecification(
    crossover_prob=0.7,
    mutation_prob=0.12,
    penalty=0.5, #irrelevante
    train_data=train_data,
    individual_max_len=0.16,
    population_size=150,
    max_generations=35,
    parents_offsprings=2,
    chromosome="BaseChromosome",
    gen="BaseGen",
    individual="BaseIndividual",
    population_updater="HybridElitism",
    parent_selector="RouletteWheel",
    penalization_function="PenaltyDistribution",
    crossover="UniformCrossover",
    mutation="ControlledMutation",
    population_generator="ApproximatedSize"
)
ga: GeneticAlgorithm = GeneticAlgorithm(problem_spec)
ga.start()
best_solution: dict = ga.get_solution()
train_labels_: list = []

for category in best_solution:
    train_labels_ += [category] * len(best_solution[category])

train_docs: list = []
for words in list(best_solution.values()):
    train_docs += words

test_labels = []
test_documents = []

for category in test_data:
    test_labels += [category.name] * category.documents_len()

for index in range(len(test_data)):
    test_documents += test_data[index].documents

text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
        ])

text_clf.fit(train_docs, train_labels_)
predicted = text_clf.predict(test_documents)

print(classification_report(test_labels, predicted, target_names=['c', 'g', 'm']))


#####joined
train_documents = []
train_labels_: list = ['soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast']

for words in list(best_solution.values()):
    train_documents.append(" ".join(words))

text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
        ])

text_clf.fit(train_documents, train_labels_)
predicted = text_clf.predict(test_documents)

print(classification_report(test_labels, predicted, target_names=['c', 'g', 'm']))
