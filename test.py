from sklearn.datasets import fetch_20newsgroups
from Email import Email

train_data = {
    'soc.religion.christian': fetch_20newsgroups(subset='train', categories=['soc.religion.christian']).data,
    'talk.politics.guns': fetch_20newsgroups(subset='train', categories=['talk.politics.guns']).data,
    'talk.politics.mideast': fetch_20newsgroups(subset='train', categories=['talk.politics.mideast']).data
}

corpus = {}
for category in train_data:
    corpus[category] = [Email(category, email) for email in train_data[category][:2]]

print(corpus['soc.religion.christian'][0])