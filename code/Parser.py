import numpy as np
import logging
import itertools
import Config
from LoggerHandler import LoggerHandler
from sklearn.feature_extraction.text import CountVectorizer
from collections import defaultdict

class DataVectorizer:
    
    # Instance methods
    original_data = {}
    parsed_data = []
    vectorizer = None
    vocabulary = {}
    
    def __init__(self, data):
        self.original_data = data
        LoggerHandler.log('Data loaded')
    
    def vectorizeData(self, stopWordsLang = Config.CORPUS_LANGUAGE, token_pattern = Config.TOKENS_PATTERN, ngrams = (1, 1)):
        self.vectorizer = CountVectorizer(
            encoding='utf-8',
            decode_error='replace',
            strip_accents='ascii',
            lowercase='true',
            stop_words=stopWordsLang,
            token_pattern=token_pattern,
            ngram_range=ngrams,
        )
        
        joined_documents = []
        for _, documents in self.original_data.items():
            joined_documents += documents
            
        self.parsed_data = self.vectorizer.fit_transform(joined_documents)
        LoggerHandler.log(f'All categories have been processed ({len(joined_documents)} documents)')
        
    def getVectorizedData(self):            
        return self.parsed_data
        
    def getCategories(self):
        return list(self.original_data.keys())
    
    def getTopWords(self, up_limit = 0, down_limit = 0):
        if len(self.vocabulary) == 0:
            sum_word_freq = np.sum(self.parsed_data.toarray(), axis=0) 
            self.vocabulary = sorted(list(zip(self.vectorizer.get_feature_names(), sum_word_freq)), key = lambda x: x[1], reverse=True)

        if(down_limit != 0 and up_limit != 0):
            return self.vocabulary[down_limit:up_limit]
        elif(down_limit != 0 and up_limit == 0):
            return self.vocabulary[down_limit:]
        elif(down_limit == 0 and up_limit != 0):
            return self.vocabulary[:up_limit]
            
        return self.vocabulary
    
    def getStopWords(self):
        return self.vectorizer.get_stop_words()
    
    def getVectorizer(self):
        return self.vectorizer
    
    def getVocabulary(self): 
        if len(self.vocabulary) == 0:
            sum_word_freq = np.sum(self.parsed_data.toarray(), axis=0) 
            self.vocabulary = sorted(list(zip(self.vectorizer.get_feature_names(), sum_word_freq)), key = lambda x: x[1], reverse=True)
        
        return self.vocabulary
    
    def getParsedDocumentAt(self, index):
        return self.parsed_data[index]
    
    def getOriginalDocumentFromParsed(self, parsed_document):
        return list(itertools.chain.from_iterable(np.vstack(self.vectorizer.inverse_transform(parsed_document))))