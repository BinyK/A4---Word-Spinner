# https://github.com/BinyK/A4-Word-Spinner.git
# Eunbin Kang

from Spinner import Spinner

def main():
    with open('essay.txt', 'r') as file:
        original_text = file.read()

    spinner = Spinner()

    print("Original :", original_text)

    for i in range(1, 4):
        changed_text = spinner.change_words(original_text)

        print("Option", i, ":", changed_text)

if __name__ == "__main__":
    main()
