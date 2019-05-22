import re
import nltk
from EmailParser import GlobalConfig
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

LEMMATIZER = WordNetLemmatizer()
STOP_WORDS = stopwords.words(GlobalConfig.CORPUS_LANGUAGE)

def cleanWord(content: str) -> str:
    content = re.sub(r'[^\w\s]', '', content)
    tokens = nltk.word_tokenize(content)
    tokens = [word for word in tokens if word.isalpha()]

    for i in range(len(tokens)):
        tokens[i] = LEMMATIZER.lemmatize(tokens[i])

    stop_words_removed = [word for word in tokens if word not in STOP_WORDS]
    return " ".join(stop_words_removed)