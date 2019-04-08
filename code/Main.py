from sklearn.datasets import fetch_20newsgroups
from Parser import DataParser

train_data = {
    'soc.religion.christian': fetch_20newsgroups(subset='train', categories=['soc.religion.christian']).data,
    'talk.politics.guns': fetch_20newsgroups(subset='train', categories=['talk.politics.guns']).data,
    'talk.politics.mideast': fetch_20newsgroups(subset='train', categories=['talk.politics.mideast']).data
}

data_parse = DataParser(train_data)
data_parse.vectorizeData()

print(data_parse.getParsedData('talk.politics.guns')[0])