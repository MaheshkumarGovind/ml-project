import nltk
from nltk.stem import WordNetLemmatizer

class WordNetLemmatizer:
    def __init__(self):
        self.lemmatizer = nltk.stem.WordNetLemmatizer()

    def lemmatize(self, word):
        return self.lemmatizer.lemmatize(word)