import random

class Spinner:
    def __init__(self):
        self.synonyms = self.load_synonyms('synonyms-simplified.txt')