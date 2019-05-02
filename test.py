from sklearn.datasets import fetch_20newsgroups
from EmailParser.Email import Email
from EmailParser.EmailEncoder import EmailEncoder
from Genetic.Simple_GA import Simple_GA
from Utilities.FileUtilities import FileUtilities


# train_data = {
#     "soc.religion.christian": fetch_20newsgroups(subset='train', categories=['soc.religion.christian']).data,
#     "talk.politics.guns": fetch_20newsgroups(subset='train', categories=['talk.politics.guns']).data,
#     "talk.politics.mideast": fetch_20newsgroups(subset='train', categories=['talk.politics.mideast']).data
# }


# corpus = {}
# for category in train_data:
#     corpus[category] = [Email(**Email.parseEmail(category, email)) for email in train_data[category]]

# FileUtilities.writeToFile(corpus, "emails.json", encoder = EmailEncoder)
train_data = FileUtilities.readJSON("emails.json", encoder = EmailEncoder.encodeEmail)
print(train_data['soc.religion.christian'][0])
