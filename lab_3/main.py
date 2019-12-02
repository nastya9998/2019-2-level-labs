"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
     def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if not self.storage:
            self.storage[word] = 0
        elif word not in self.storage:
            self.storage[word] = max(self.storage.values()) + 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if word not in self.storage:
            return -1
        else:
            return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if not isinstance(id, int):
            return 'UNK'
        for key, value in self.storage.items():
            if value == id:
                return key
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if not isinstance(corpus, tuple):
            return {}
        for word in corpus:
            self.storage[word] = self.put(word)
        #вызывает путAnn

class NGramTrie:
    def fill_from_sentence(self, sentence: tuple) -> str:
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass


def encode(storage_instance, corpus) -> list:
    num_corpus = []
    for sent in corpus:
        sen_corpus = []
        for word in sent:
            num = storage_instance[word]
            sen_corpus.append(num)
        num_corpus.append(sen_corpus)
    return num_corpus


def split_by_sentence(text: str) -> list:
        if not isinstance(text, str) or not text:
        return []
    text = text.lower()
    text = text.replace('\n', '')
    text = text.replace('!', '.')
    text = text.replace('?', '.')
    text_list = text.split('. ')
    if '.' not in text:
        return []
    clear_text = []
    for sen in text_list:
        for s in sen:
            if not s.isalpha() and s != ' ':
                sen = sen.replace(s, '')
        sen_list = sen.split()
        clear_text.append(sen_list)
    if [] in clear_text:
        return []
    res_text = []
    for i in clear_text:
        list_text = ['<s>']
        list_text.extend(i)
        list_text.append('</s>')
        res_text.append(list_text)
    return res_text
