import time
from sklearn.feature_extraction.text import CountVectorizer

class DataParser:
    
    #Instance methods
    original_data = {}
    parsed_data = {}
    
    def __init__(self, data):
        self.original_data = data
        self.log('Data loaded!')
    
    def vectorizeData(self, stopWordsLang = 'english', token_pattern = '(?u)\\b\\w\\w+\\b', ngrams = (1, 1)):
        vectorizer = CountVectorizer(
            encoding = 'utf-8', 
            decode_error = 'replace', 
            strip_accents = 'ascii', 
            lowercase = 'true',
            stop_words = stopWordsLang,
            token_pattern = token_pattern,
            ngram_range = ngrams,
        )
        
        for key, value in self.original_data.items():
            self.parsed_data[key] = vectorizer.fit_transform(value)
            self.log('{category} processed'.format(category = key))
        
    def log(self, msg):
        print("{time} [PARSER] -> {msg}".format(msg = msg, time = time.strftime("%H:%M:%S")))
        
    def getParsedData(self, category):
        return self.parsed_data[category]
    
    def getCategories(self):
        return list(self.parsed_data.keys())