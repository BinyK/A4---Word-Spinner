import random

class Spinner:
    def __init__(self):
        self.synonyms = self.load_synonyms('synonyms-simplified.txt')

    def load_synonyms(self, filename):
        synonyms = {}
        with open(filename, 'r') as file:
            for line in file:
                word, synonyms_str = line.strip().split(':')  # strip & split 사용
                synonyms[word] = synonyms_str.split(',')
        return synonyms
