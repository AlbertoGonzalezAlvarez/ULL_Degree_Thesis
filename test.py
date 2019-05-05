from sklearn.datasets import fetch_20newsgroups
from EmailParser.Email import Email
from EmailParser.EmailEncoder import EmailEncoder
from Genetic.Simple_GA import Simple_GA
from Utilities.FileUtilities import FileUtilities

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
    FileUtilities.writeToFile(train_data_corpus, "test_data.json", encoder = EmailEncoder)

train_data_JSON = FileUtilities.readJSON("train_data.json")
test_data_JSON = FileUtilities.readJSON("train_data.json")

train_data = Email.from_json(train_data_JSON)
test_data = Email.from_json(test_data_JSON)

genetic = Simple_GA(train_data, test_data, 0.1, 20)
genetic.startUpGA()