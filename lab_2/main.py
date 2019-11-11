"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    list_0 = []
    if isinstance(num_rows, int) and isinstance(num_cols, int):
        for i in range(num_rows):
            list_0.append([0] * num_cols)
    return list_0


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if not isinstance(edit_matrix, tuple) or edit_matrix == ():
        return []
    edit_matrix = list(edit_matrix)
    a = [[]]
    none_matrix = a * len(edit_matrix)
    if edit_matrix == none_matrix:
        return edit_matrix
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int):
        return edit_matrix
    for i in range(1, len(edit_matrix)):
        edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight
    for i in range(1, len(edit_matrix[0])):
        edit_matrix[0][i] = edit_matrix[0][i - 1] + add_weight
    return edit_matrix


def minimum_value(numbers: tuple) -> int:
    if isinstance(numbers,tuple):
        return min(numbers)
    else:
        return False


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    if not isinstance(edit_matrix, tuple):
        return []
    edit_matrix = list(edit_matrix)
    if type(add_weight) == int and type(remove_weight) == int and type(substitute_weight) == int and type(original_word) == str \
            and type(target_word) == str and original_word != '' and target_word != '':
        target_word = ' ' + target_word
        original_word = ' ' + original_word
        for i in range(1, len(edit_matrix)):
            for j in range(1, len(edit_matrix[0])):
                m_1 = edit_matrix[i - 1][j] + remove_weight
                m_2 = edit_matrix[i][j - 1] + add_weight
                m_3 = edit_matrix[i - 1][j - 1]
                if original_word[i] != target_word[j]:
                    m_3 += substitute_weight
                tuple_x = (m_1, m_2, m_3)
                min_m = minimum_value(tuple_x)
                edit_matrix[i][j] = min_m
    return edit_matrix


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if not isinstance(original_word, str) or not isinstance(target_word, str) or not isinstance(add_weight, int) \
            or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int):
        return -1
    matrix = generate_edit_matrix(len(original_word) + 1, len(target_word) + 1)
    matrix_i = initialize_edit_matrix(tuple(matrix), add_weight, remove_weight)
    matrix_res = fill_edit_matrix(tuple(matrix_i), add_weight, remove_weight, substitute_weight, original_word, target_word)
    way = matrix_res[-1][-1]
    return way


def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    if not isinstance(edit_matrix, tuple) or not isinstance(path_to_file, str):
        return None
    file_save = open(path_to_file, 'w')
    cont = ''
    for stroka in edit_matrix:
        for el in stroka:
            el = str(el)
            cont += el + ','
        file_save.write(cont + '\n')
    file_save.close()


def load_from_csv(path_to_file: str) -> list:
    if not isinstance(path_to_file, str):
       return []
    a = open(path_to_file)
    matrix = []
    for line in a:
        row = []
        new_line = line.replace(',', '')
        for i in new_line:
            i = int(i)
            row.append(i)
    matrix.append(row)
    a.close()
    return matrix

