import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.corpus import stopwords
import string

def readJsonFile(file):
    with open(file) as file:
        data = []
        for line in file:
            data.append(json.loads(line)["short_description"])
    return data

def text_process(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
    return " ".join(text)

# def sparseVectorPrinter(v): 
#     print({n: val for n, val in enumerate(v) if val})

data = readJsonFile('data/news.json')

bagOfWords = []

for row in data:
    bagOfWords.append(text_process(row))

print(bagOfWords[0])

vectorizer = CountVectorizer(ngram_range=(1, 1))
wordSparseVector = vectorizer.fit_transform(bagOfWords)

for word in vectorizer.vocabulary_:
    print('{{{word}: {freq}}}'.format(word = word, freq = vectorizer.vocabulary_[word]))

tf_transformer = TfidfTransformer(use_idf=False).fit(wordSparseVector)
X_train_tf = tf_transformer.transform(wordSparseVector)

print(X_train_tf)

