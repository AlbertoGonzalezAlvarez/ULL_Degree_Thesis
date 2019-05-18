from sklearn.datasets import fetch_20newsgroups
from EmailParser.Email import Email
from Genetic.Chromosome import Chromosome
from EmailParser.EmailEncoder import EmailEncoder
from Genetic.Simple_GA import Simple_GA
from Utilities.FileUtilities import FileUtilities
from EmailParser.DataCategories import DataCategories
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

train_data = [DataCategories.addTrainCategory(category, train_data_dict[category], ['content']) for category in train_data_dict]
test_data = [DataCategories.addTestCategory(category, test_data_dict[category], ['content']) for category in test_data_dict]

# print(train_data[0].corpus)
# genetic_spec = GAData(train_data, test_data, 0.1, 2, 2)
parent_2 = Chromosome([3, 1, 4], 5)
print(len(parent_2))
# print(parent_2)
# parent_2[0:0] = Gen(GEN_STATE.REMOVED)
# print(parent_2)
# print(parent_2.gensBetween(2, 3))
# print(parent_2[2:3])
#
# parent_2.gensBetween(1, 2) = [4]