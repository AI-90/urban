class WordsFinder:
    def __init__(self, *names):
        (self.file_names) = []
        for name in names:
            self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        cut = (',', '.', '=', '!', '?', ';', ':', ' - ')
        for name in self.file_names:
            list_words = []
            with open(name, encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    for symbol in cut:
                        line = line.replace(symbol,' ')
                    for word in line.split():
                        list_words.append(word)
                all_words[name] = list_words
        return all_words

    def find(self, word):
        word = word.lower()
        f_dict = {}
        for name, words in self.get_all_words().items():
            number = 1
            for d_word in words:
                if word == d_word:
                    f_dict[name] = number
                    break
                number += 1
        return f_dict

    def count(self, word):
        word = word.lower()
        c_dict = {}
        for name, words in self.get_all_words().items():
            count = 0
            for d_word in words:
                if word == d_word:
                    count += 1
            c_dict[name] = count
        return c_dict




finder2 = WordsFinder('test_file.txt','test_file2.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего