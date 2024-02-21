# https://github.com/BinyK/A4-Word-Spinner.git
# Eunbin Kang

from Spinner import Spinner

def main():
    with open('essay.txt', 'r') as file:
        original_text = file.read()

    spinner = Spinner()

    print("Original :", original_text)