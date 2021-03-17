"""
Huffman Encoder
Author: Danmar and Lidi
"""

'''
    Function which gets a data and returns the frequency of each char
'''


def create_freq_table(my_data):
    freq_table = {}
    for symbol in my_data:
        if symbol not in freq_table.keys():
            freq_table[symbol] = 1
        else:
            freq_table[symbol] += 1
    for symbol in freq_table.keys():
        freq_table[symbol] = freq_table[symbol] / len(my_data)  # total frequencies is 1
    return freq_table


'''
    Function which gets a list and return a set
'''


def list2set(my_list):
    final_set = []
    for element in my_list:
        if element not in final_set:
            final_set.append(element)
    return final_set


'''
    Function which gets a data and frequency table and returns it as an heap.
'''


def create_priority_list(freq_table):
    values = []
    while len(freq_table.keys()) > 1:
        first_min = min(freq_table, key=freq_table.get)
        first_min_value = freq_table[first_min]
        freq_table.pop(first_min)

        second_min = min(freq_table, key=freq_table.get)
        second_min_value = freq_table[second_min]
        freq_table.pop(second_min)

        freq_table[first_min + second_min] = first_min_value + second_min_value
        new_val = str(first_min) + str(second_min)
        values.append(first_min)
        values.append(second_min)
        values.append(new_val)

    values.reverse()  # up-down
    return list2set(values[1:])


class EncodeTable:
    def __init__(self, input_string):
        self._input_string = input_string

        freq_table = create_freq_table(input_string)
        priority_list = create_priority_list(freq_table)
        self._initialize_encode_table(priority_list)

    def encode(self):
        translation = ''
        for char in self._input_string:
            translation += str(self._table[char])
        return translation

    def __str__(self):
        lines = []

        for symbol, value in self._table.items():
            symbol_name = "space" if symbol == ' ' else symbol

            line = f"{symbol_name}: {value}"
            lines.append(line)

        return '\n'.join(lines)

    def _initialize_encode_table(self, priority_list):
        initial_encode_table = EncodeTable._generate_initial_table(priority_list)

        self._table = {}
        single_char_symbols = [symbol for symbol in priority_list if len(symbol) == 1]

        for char in single_char_symbols:
            for symbol in initial_encode_table:
                if char in symbol:
                    if char in self._table:
                        self._table[char] += str(initial_encode_table[symbol])
                    else:
                        self._table[char] = str(initial_encode_table[symbol])

    @staticmethod
    def _generate_initial_table(priority_list):
        encode_table = {}
        for i in range(len(priority_list)):
            if i % 2 == 0:
                encode_table[priority_list[i]] = 0
            else:
                encode_table[priority_list[i]] = 1
        return encode_table
