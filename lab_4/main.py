import math

REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    if not isinstance(texts, list):
        return []
    list_texts = []
    for txt in texts:
        if isinstance(txt, str):
            c_n_txt = ''
            n_txt = txt.lower()
            n_txt = n_txt.replace('br', ' ')
            for sign in n_txt:
                if sign.isalpha() or sign == ' ':
                    c_n_txt += sign
            list_text = c_n_txt.split()
            list_texts.append(list_text)
    return list_texts


class TfIdfCalculator:
    def __init__(self, corpus):
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.corpus = corpus

    def calculate_tf(self):
        if isinstance(self.corpus, list):
            for txt in self.corpus:
                if isinstance(txt, list):
                    clean_text = []
                    for word in txt:
                        if isinstance(word,str):
                            clean_text.append(word)
                    tf_dict = {word: clean_text.count(word)/len(clean_text) for word in clean_text}
                    self.tf_values.append(tf_dict)

    def calculate_idf(self):
        if not isinstance(self.corpus, list):
            return []
        clean_corpus = []
        for txt in self.corpus:
            if isinstance(txt, list):
                clean_corpus.append(txt)
        for txt in clean_corpus:
            for word in txt:
                if not isinstance(word, str):
                    continue
                number = 0
                for txt in clean_corpus:
                    if word in txt:
                        number += 1
                self.idf_values[word] = math.log(len(clean_corpus) / number)

    def calculate(self):
        if not self.tf_values or not isinstance(self.tf_values, list):
            return []
        if not self.idf_values or not isinstance(self.idf_values, dict):
            return []
        for txt in self.tf_values:
            dict_for_tf_idf = {}
            for k, v in txt.items():
                dict_for_tf_idf[k] = v * self.idf_values[k]
            self.tf_idf_values.append(dict_for_tf_idf)

    def report_on(self, word, document_index):
        if not isinstance(self.tf_idf_values, list) or document_index > len(self.tf_idf_values) - 1:
            return ()
        if not isinstance(word, str):
            return ()
        if word in self.tf_idf_values[document_index]:
            top_dict = list(self.tf_idf_values[document_index].items())
            top_dict = sorted(top_dict, key=lambda x: x[1], reverse=True)
            index = -1
            for pair_tuple in top_dict:
                if word in pair_tuple:
                    index = top_dict.index(pair_tuple)
                    break
            our_tf_idf = self.tf_idf_values[document_index].get(word)
            our_tuple = (our_tf_idf, index)
            return our_tuple


if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
