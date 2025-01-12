import re
class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words = []

                for line in file:
                    re.sub(r'[.,!?\'\"]', '', line)
                    cleaned_line = line.lower()
                    words += cleaned_line.split()
                all_words[name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            index = words.index(word.lower())
            result[name] = index + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            count = words.count(word.lower())
            result[name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

import re
class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words = []

                for line in file:
                    re.sub(r'[.,!?\'\"]', '', line)
                    cleaned_line = line.lower()
                    words += cleaned_line.split()
                all_words[name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            index = words.index(word.lower())
            result[name] = index + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            count = words.count(word.lower())
            result[name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))



