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

corpus = {}   
for category in train_data:
    corpus[category] = [Email(category, email) for email in train_data[category][:2]]

# data_parse = DataVectorizer(email)
# data_parse.vectorizeData()
# 
# print(train_data['soc.religion.christian'][162])
# 
#print(data_parse.getOriginalDocumentFromParsed(data_parse.getParsedDocumentAt(2)))
