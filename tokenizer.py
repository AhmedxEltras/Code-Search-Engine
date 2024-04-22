import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class WordTokenizer:
    def tokenize(self, query):
        return nltk.word_tokenize(query)

class StopwordTokenizer:
    def __init__(self):
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def tokenize(self, query):
        tokens = nltk.word_tokenize(query)
        return [token for token in tokens if token.lower() not in self.stop_words]

class StemmingTokenizer:
    def __init__(self):
        self.porter_stemmer = PorterStemmer()

    def tokenize(self, query):
        tokens = nltk.word_tokenize(query)
        return [self.porter_stemmer.stem(token) for token in tokens]
