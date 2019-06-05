import re
import nltk
from EmailParser import GlobalConfig
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

LEMMATIZER = WordNetLemmatizer()
STOP_WORDS = stopwords.words(GlobalConfig.CORPUS_LANGUAGE)

def cleanWord(content: str) -> str:
    content = re.sub(r'[^\w\s]|\w*\d\w*', '', content)
    tokens = nltk.word_tokenize(content)
    tokens = [word.lower() for word in tokens if word.isalpha() and len(word) > 2]

    for i in range(len(tokens)):
        tokens[i] = LEMMATIZER.lemmatize(tokens[i], pos=__wordCategory__(pos_tag(tokens[i])))

    stop_words_removed = [word for word in tokens if word not in STOP_WORDS]

    return " ".join(stop_words_removed)

def __wordCategory__(penntag):
    morphy_tag = {'NN':'n', 'JJ':'a',
                  'VB':'v', 'RB':'r'}
    try:
        return morphy_tag[penntag[:2]]
    except:
        return 'n'