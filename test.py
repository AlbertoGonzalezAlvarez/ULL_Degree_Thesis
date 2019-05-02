from sklearn.datasets import fetch_20newsgroups
from EmailParser.Email import Email
from Genetic.Simple_GA import Simple_GA
from Utilities.FileUtilities import FileUtilities
import os

train_data = {
    'soc.religion.christian': fetch_20newsgroups(subset='train', categories=['soc.religion.christian']).data,
    'talk.politics.guns': fetch_20newsgroups(subset='train', categories=['talk.politics.guns']).data,
    'talk.politics.mideast': fetch_20newsgroups(subset='train', categories=['talk.politics.mideast']).data
}


corpus = {}
for category in train_data:
    corpus[category] = [Email(category, email) for email in train_data[category]]

FileUtilities.writeToFile(corpus, "emails.json")

FileUtilities.writeToFile(train_data, "emails.txt")