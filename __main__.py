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
    crossover_prob=0.7,
    mutation_prob=0.07,
    penalty=0.5, #irrelevante
    train_data=train_data,
    individual_max_len=0.25,
    population_size=100,
    max_generations=500,
    parents_offsprings=2,
    chromosome="BaseChromosome",
    gen="BaseGen",
    individual="BaseIndividual",
    population_updater="HybridElitism",
    parent_selector="Tournament",
    penalization_function="PenaltyDistribution",
    crossover="UniformCrossover",
    mutation="ControlledMutation",
    population_generator="ApproximatedSize"
)

ga: GeneticAlgorithm = GeneticAlgorithm(problem_spec)
ga.start()