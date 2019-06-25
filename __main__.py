from EmailParser import EmailEncoder, DataCategory
from Utilities import FileUtilities
from sklearn.datasets import fetch_20newsgroups
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
    crossover_prob=1.0,
    mutation_prob=0.15,
    penalty= 0.01,
    train_data=train_data,
    individual_max_len=0.1,
    population_updater="BestsIndividuals",
    population_generator="ApproximatedSize",
    parent_selector="RouletteWheel",
    population_size=20,
    max_generations=400
)

ga: GeneticAlgorithm = GeneticAlgorithm(problem_spec)
ga.start()