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


    def change_words(self, text):
        words = text.split()
        new_text = ""
        for word in words:
            if word.lower() in self.synonyms:
                if random.randint(1, 100) > 50:
                    new_text += random.choice(self.synonyms[word.lower()]) + " " 
                else:
                    new_text += word + " "   # EX) text = "I am" followed by text += "David",  {'kid': ['child', 'goat']} 
        return new_text

