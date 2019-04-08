import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.corpus import stopwords
from sklearn.naive_bayes import MultinomialNB
import string

def readJsonFile(file, *fieldsToRead):
    with open(file) as file:
        data = []
        for line in file:
            fields = ""
            for field in fieldsToRead:
                fields += " " + json.loads(line).get(field)
            data.append(fields) 
    return data

def text_process(text):
    # Remove puntuaction
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
    return " ".join(text)

def vectorizeDataClass(categories, dataClass):
    vectorized = []
    for category in dataClass:
        vectorized.append(categories[category])
    
    return vectorized
        
    
# def sparseVectorPrinter(v): 
#     print({n: val for n, val in enumerate(v) if val})


data = readJsonFile('data/news.json', "headline", "short_description")
print(data[0])
dataClass = readJsonFile('data/news.json', "category")[0:50000]
categories = dict([(y,x+1) for x,y in enumerate(sorted(set(dataClass)))])

vectorizedDataClass = vectorizeDataClass(categories, dataClass)

bagOfWords = []
  
for row in data:
    bagOfWords.append(text_process(row))
  
train = bagOfWords[0:50000]
  
count_vect = CountVectorizer(ngram_range = (1, 1))
X_train_counts = count_vect.fit_transform(train)
  
# for word in vectorizer.vocabulary_:
#     print('{{{word}: {freq}}}'.format(word = word, freq = vectorizer.vocabulary_[word]))
  
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
  
clf = MultinomialNB().fit(X_train_tfidf, vectorizedDataClass)

toPredict = bagOfWords[50000:50010]
X_new_counts = count_vect.transform(toPredict)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
  
predicted = clf.predict(X_new_tfidf)

categories = list(categories)
print(categories)
for doc, category in zip(toPredict[:10], predicted[:10]):
    print('%r => %s' % (doc, categories[category - 1]))