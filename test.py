from sklearn.datasets import fetch_20newsgroups
from EmailParser.Email import Email
from Genetic.Chromosome import Chromosome
from EmailParser.EmailEncoder import EmailEncoder
from Genetic.Simple_GA import Simple_GA
from Utilities.FileUtilities import FileUtilities
from EmailParser.DataCategory import DataCategory
from Genetic.GAData import GAData
from Genetic.Gen import Gen, GEN_STATE

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

# print(train_data[0].corpus)
genetic_spec = GAData(train_data, test_data, 0.1, 2, 2)
genetic_alg = Simple_GA(genetic_spec)
genetic_alg.startUpGA()
# parent_2 = Chromosome([3, 4, 2], 5)
# parent_1 = Chromosome([0, 1, 2], 5)

# print(parent_2)
# parent_2[3] = parent_1[0:0] # [3, 4, 2] -> [4, 2, 0]
# parent_2[2:2] = parent_1[3] # [3, 4, 2] -> [3, 4]
# parent_2[1:2] = parent_1[0:1] # [3, 4, 2] -> [3, 4, 0, 1] !!
# parent_2[1] = parent_1[1] # [3, 4, 2] -> [3, 4, 2, 1]
# print(parent_2)
# print(parent_1[0:0])
# print(parent_1[0:1])
# print(parent_1[1:1])
