from sklearn.datasets import fetch_20newsgroups
from EmailParser import EmailEncoder, DataCategory
from Utilities import FileUtilities
from Genetic.Simple_GA_Specification import SimpleGASpecification
from Genetic.Simple_GA_Solver import Simple_GA

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
                                     mutation_rate = 0.1,
                                     populationSize = 20,
                                     maxIndividualFeatures = 20,
                                     fitness_penalization = 0.7,
                                     cutting_points = 7
                                     )

genetic_alg = Simple_GA(genetic_spec)
genetic_alg.startUpGA()
