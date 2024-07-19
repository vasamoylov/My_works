class WordsFinder:
    def __init__(self, *files):
        self.file_names = [*files]
    def get_all_words(self):
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                line = file.read().lower()
            for i in symbols:
                line = line.replace(i, '')
            line = line.split()
            all_words[name] = line
        return all_words

    def find(self, word):
        words = self.get_all_words()
        dic = {}
        count = 0
        for k, v in words.items():
            for i in v:
                count += 1
                if i == word.lower():
                    dic[k] = count
                    break
        return dic
    def count(self, word):
        words = self.get_all_words()
        dic = {}
        count = 0
        for k, v in words.items():
            for i in v:
                if i == word.lower():
                    count += 1
            dic[k] = count
        return dic

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
                