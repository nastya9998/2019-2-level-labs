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

class NGramTrie:
    def __init__(self, n):
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.size = n

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'ERROR'
        for i in range(len(sentence)):
            if i < len(sentence) - self.size:
                words_gram = sentence[i: i + self.size]
                if words_gram in self.gram_frequencies:
                    self.gram_frequencies[words_gram] += 1
                else:
                    self.gram_frequencies[words_gram] = 1
            elif i == len(sentence) - self.size:
                words_gram = sentence[i:]
                if words_gram in self.gram_frequencies:
                    self.gram_frequencies[words_gram] += 1
                else:
                    self.gram_frequencies[words_gram] = 1
        return 'OK'

    def calculate_log_probabilities(self):
        for pair in self.gram_frequencies:
            w_n_1 = pair[0:self.size - 1]
            count = 0
            for key in self.gram_frequencies:
                if w_n_1 == key[0:self.size - 1]:
                    count += self.gram_frequencies[key]
            prob = math.log(self.gram_frequencies[pair]/count)
            self.gram_log_probabilities[pair] = prob

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple) or not prefix:
            return []
        if len(prefix) != self.size - 1:
            return []
        sentence = []
        prefix_list = list(prefix)
        sentence.extend(prefix_list)
        beginnings = []
        for gram in self.gram_log_probabilities:
            beginnings.append(gram[0: self.size - 1])
        while prefix in beginnings:
            pro = []
            for k, v in self.gram_log_probabilities.items():
                if prefix == k[0: self.size - 1]:
                    pro.append((v, k))
            pro.sort(reverse=True)
            affix = pro[0][1][-1]
            sentence.append(affix)
            prefix = pro[0][1][1:]
        return sentence



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
