import Config
import re
import nltk
from Log import LoggerHandler
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

language = None
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words(Config.CORPUS_LANGUAGE)


class Email:
    category = None
    from_email = None
    subject_ = None
    organization_ = None
    content_ = None
    errors = 0

    def __init__(self, category, message):
        self.category = category
        self.__extractHeaders(message)

    def __str__(self):
        _from_ = f'From: {self.from_email}'
        _subject_ = f'\nSubject: {self.subject}'
        _organization_ = f'\nOrganization: {self.organization_}'
        _content_ = f'\nContent: {self.content_[:100]}...'
        _category_ = f'\nCategory: {self.category}'

        return _from_ + _subject_ + _organization_ + _content_

    def getSender(self):
        return self.from_email

    def __extractHeaders(self, message):
        searchHeader = re.search(Config.EMAIL_HEADER_REGEX, message)

        if searchHeader != None:
            searchHeader = searchHeader.group()
            self.from_email = self.__getEmailFromHeader(searchHeader)
            self.subject = self.__getSubjectFromHeader(searchHeader)
            self.organization_ = self.__getOrganization(searchHeader)

            content = message.replace(searchHeader, "")
            self.content_ = self.getContent(content)
        else:
            Email.errors += 1
            LoggerHandler.error(f'Error while reading email header. Error count = {Email.errors}')

    def getContent(self, content):
        return self.__removeMeaningLessWords(content)

    def __getEmailFromHeader(self, header):
        found_email = re.search(Config.FROM_EMAIL_REGEX, header).group().lower()
        from_email = re.search(Config.EMAIL_ADRESS, found_email).group()

        return from_email

    def __getSubjectFromHeader(self, header):
        found_subject = re.search(Config.SUBJECT_REGEX, header).group(2).lower()

        return self.__removeMeaningLessWords(found_subject)

    def __getOrganization(self, header):
        found_organization = re.search(Config.ORGANIZATION_REGEX, header)

        if found_organization != None:
            return found_organization.group(2)

        return None

    def __removeMeaningLessWords(self, content):
        content = re.sub(r'[^\w\s]', '', content)
        tokens = nltk.word_tokenize(content)
        tokens = [word for word in tokens if word.isalpha()]

        for i in range(len(tokens)):
            tokens[i] = lemmatizer.lemmatize(tokens[i])

        stop_words_removed = [word for word in tokens if word not in stop_words]
        return " ".join(stop_words_removed)