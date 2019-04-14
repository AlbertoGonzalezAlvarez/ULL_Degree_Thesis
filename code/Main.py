from sklearn.datasets import fetch_20newsgroups
from Parser import DataVectorizer
from Email import Email
import random
import Config

train_data = {
    'soc.religion.christian': fetch_20newsgroups(subset='train', categories=['soc.religion.christian']).data,
    'talk.politics.guns': fetch_20newsgroups(subset='train', categories=['talk.politics.guns']).data,
    'talk.politics.mideast': fetch_20newsgroups(subset='train', categories=['talk.politics.mideast']).data
}

corpus = []

for category in train_data:
    corpus = corpus + train_data[category]
    
email = []
for document in corpus:
    email.append(Email(document))
    
#email = Email(train_data['soc.religion.christian'][random.randint(0, len(train_data['soc.religion.christian']))])
# data_parse = DataVectorizer(train_data)
# data_parse.vectorizeData()
# 
# print(train_data['soc.religion.christian'][162])
# 
# print(data_parse.getOriginalDocumentFromParsed(data_parse.getParsedDocumentAt(2)))
