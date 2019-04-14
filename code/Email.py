import Config
import re
import nltk
from LoggerHandler import LoggerHandler
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer 

language = None
lemmatizer = WordNetLemmatizer() 
stop_words = stopwords.words(Config.CORPUS_LANGUAGE)

class Email:
    
    from_email = None
    subject_ = None
    organization_ = None
    content_ = None
    errors = 0
    
    def __init__(self, message):
        self.extractHeaders(message)
    
    def getSender(self):
        return self.from_email
    
    # Private
    def extractHeaders(self, message):        
        searchHeader = re.search(Config.EMAIL_HEADER_REGEX, message)
        
        if searchHeader != None:
            searchHeader = searchHeader.group()
            self.from_email = self.getEmailFromHeader(searchHeader)
            self.subject = self.getSubjectFromHeader(searchHeader)
            self.organization_ = self.getOrganization(searchHeader)
            
            content = message.replace(searchHeader, "")
            self.content_ = self.getContent(content)
        else:
            Email.errors += 1
            LoggerHandler.error(f'Error while reading email header. Error count = {Email.errors}')
        
    def getContent(self, content):
        return self.removeMeaningLessWords(content)
        
    # Private
    def getEmailFromHeader(self, header):
        found_email = re.search(Config.FROM_EMAIL_REGEX, header).group().lower()
        from_email = re.search(Config.EMAIL_ADRESS, found_email)
        
        return from_email
    
    # Private    
    def getSubjectFromHeader(self, header):
        found_subject = re.search(Config.SUBJECT_REGEX, header).group(2).lower()
        self.removeMeaningLessWords(found_subject)
    
    # Private
    def getOrganization(self, header):
        found_organization = re.search(Config.ORGANIZATION_REGEX, header)

        if found_organization != None:
            return found_organization.group(2)
        
        return None
    
    # Private            
    def removeMeaningLessWords(self, content):
        content = re.sub(r'[^\w\s]', '', content)
        tokens = nltk.word_tokenize(content)
        tokens = [word for word in tokens if word.isalpha()]
        
        for i in range(len(tokens)):
            tokens[i] = lemmatizer.lemmatize(tokens[i])
            
        stop_words_removed = [word for word in tokens if word not in stop_words]
        return " ".join(stop_words_removed)