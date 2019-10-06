"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def read_from_file(file_name, stroki):
    text = ''
    if type(stroki) == int and type(file_name) == str:
        f = open(file_name)
        for i in range(stroki):
            text += f.readline()
        f.close()
    return text


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    words_count = {}
    if type(text) == str:
        text = text.lower()
        real_text = ''
        text = text.replace('\n', ' ')
        for s in text:
            if s.isalpha() or s == ' ':
                real_text += s
        res = real_text.split(' ')
        for i in res:
            if i not in words_count and i != '':
                words_count[i] = 1
            elif i in words_count:
                words_count[i] += 1
    return words_count


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    without_sw = {}
    work_list_sw = []
    if type(frequencies) == dict and type(stop_words) == tuple:
        for word in stop_words:
            if type(word) == str:
                work_list_sw.append(word)
        for key in frequencies.keys():
            if type(key) == str and key not in work_list_sw:
                    without_sw[key] = frequencies.get(key)
    return without_sw


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    result = ()
    if type(frequencies) == dict and type(top_n) == int:
        if len(frequencies) < top_n:
            top_n = len(frequencies)
        for i in range(top_n):
            max = 0
            for k, v in frequencies.items():
                if v > max:
                    max = v
                    its_name = k
            frequencies.pop(its_name)
            result += (its_name,)
    return result


def write_to_file(path_to_file: str, content: tuple):
    if type(path_to_file) == str and type(content) == tuple:
        f = open(path_to_file, 'a')
        for i in content:
            f.write(i)
        f.close()

