import nltk
from tokenizer import WordTokenizer, StopwordTokenizer, StemmingTokenizer
from file_search import search_files_with_wildcard, search_files_with_phrase, search_files_approximate

class SearchEngine:
    def __init__(self):
        # Initialize NLTK resources
        nltk.download('punkt')
        nltk.download('stopwords')
        
        # Initialize tokenizers
        self.word_tokenizer = WordTokenizer()
        self.stopword_tokenizer = StopwordTokenizer()
        self.stemming_tokenizer = StemmingTokenizer()

    def search_files(self, directory, query, search_method, tokenizer_type):
        if tokenizer_type == "Word Tokenizer":
            tokens = self.word_tokenizer.tokenize(query)
        elif tokenizer_type == "Stopword Tokenizer":
            tokens = self.stopword_tokenizer.tokenize(query)
        elif tokenizer_type == "Stemming Tokenizer":
            tokens = self.stemming_tokenizer.tokenize(query)
        else:
            tokens = nltk.word_tokenize(query)
        
        if search_method == "Wild Card":
            return search_files_with_wildcard(directory, tokens)
        elif search_method == "Phrase":
            return search_files_with_phrase(directory, tokens)
        elif search_method == "Approximate":
            return search_files_approximate(directory, tokens)
        else:
            return []  # Placeholder for implementing boolean search logic
