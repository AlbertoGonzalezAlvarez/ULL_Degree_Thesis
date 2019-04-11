import numpy as np
import logging
from LoggerHandler import LoggerHandler
from sklearn.feature_extraction.text import CountVectorizer
from collections import defaultdict

class DataParser:
    
    # Instance methods
    original_data = {}
    parsed_data = {}
    vectorizer = None
    vocabulary = {}
    
    def __init__(self, data):
        self.original_data = data
        LoggerHandler.log('Data loaded')
    
    def vectorizeData(self, stopWordsLang='english', token_pattern='(?u)\\b\\w\\w\\w+\\b', ngrams=(1, 1)):
        self.vectorizer = CountVectorizer(
            encoding='utf-8',
            decode_error='replace',
            strip_accents='ascii',
            lowercase='true',
            stop_words=stopWordsLang,
            token_pattern=token_pattern,
            ngram_range=ngrams,
        )
        
        for key, value in self.original_data.items():
            self.parsed_data[key] = self.vectorizer.fit_transform(value)
            LoggerHandler.log('{category} processed'.format(category=key))
        
    def getParsedData(self, category):
        return self.parsed_data[category]
    
    def getCategories(self):
        return list(self.parsed_data.keys())
    
    def getVocabulary(self, n_top_words = 0, categories = []):
        categories = list(self.parsed_data.keys()) if len(categories) == 0 else categories
        
        if (len(self.vocabulary) != len(categories)):
            for category in categories:
                sum_words = self.parsed_data[category].sum(axis=0) 
                self.vocabulary[category] = []
                
                for word, index in self.vectorizer.vocabulary_.items():
                    if(index < sum_words.size and sum_words[0, index]):
                        self.vocabulary[category].append((word, sum_words[0, index]))
                
                self.vocabulary[category] = sorted(self.vocabulary[category], key = lambda x: x[1], reverse=True)

        desired_categories = {}
        for category in categories:
            if(n_top_words != 0):
                try:
                    if(n_top_words > len(self.vocabulary[category])):
                        raise IndexError
                    
                    desired_categories[category] = self.vocabulary[category][:n_top_words]
                except IndexError:
                    LoggerHandler.warning(f'It\'s not posible to fetch the {n_top_words} top words of ' + 
                               f'{category}, the {len(self.vocabulary[category])} top words will be returned instead')
                
                    desired_categories[category] = self.vocabulary[category]
            else:
                desired_categories[category] = self.vocabulary[category]
            
        return desired_categories
    
    def getStopWords(self):
        return self.vectorizer.get_stop_words()