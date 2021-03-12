
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
    Function which gets a data and returns the frequency of each symbol
'''


def create_freq_table(my_data):
    freq_table = {}
    for symbol in my_data:
        if symbol not in freq_table.keys():
            freq_table[symbol] = 1
        else:
            freq_table[symbol] += 1
    for symbol in freq_table.keys():
        freq_table[symbol] = freq_table[symbol] / len(my_data) # total frequencies is 1
    return freq_table

'''
    Function which gets a data and frequency table and returns it as an heap.
'''

def create_priority_list(my_data, freq_table):
    values = []
    while len(freq_table.keys()) > 1:
        first_min = min(freq_table, key=freq_table.get)
        first_min_value = freq_table[first_min]
        freq_table.pop(first_min)

        second_min = min(freq_table, key=freq_table.get)
        second_min_value = freq_table[second_min]
        freq_table.pop(second_min)

        freq_table[first_min+second_min] = first_min_value + second_min_value
        new_val = str(first_min) + str(second_min)
        values.append(first_min)
        values.append(second_min)
        values.append(new_val)

    values.reverse() #up-down
    return list2set(values[1:])


'''
    Function which gets a data and priority list and based on that creates encode_table
'''

def create_encode_table(my_data, priority_list):
    encode_table = {}
    for i in range(len(priority_list)):
        if i%2 == 0:
            encode_table[priority_list[i]] = 0
        else:
            encode_table[priority_list[i]] = 1
    final_encode_table = {}
    for symbol in [i for i in priority_list if len(i) == 1]:
        for element in encode_table:
            if symbol in element and symbol in final_encode_table:
                final_encode_table[symbol] += str(encode_table[element])
            if symbol in element and symbol not in final_encode_table:
                final_encode_table[symbol] = str(encode_table[element])

    return final_encode_table

'''
    Function which gets a data and encode_table and based on that translates the data to binary code
'''

def encode(my_data, encode_table):
    translation = ''
    for symbol in my_data:
        translation += str(encode_table[symbol])
    return translation


'''
    Function which gets a data and returns it hoffman encoded
'''

def huffman(my_data):
    freq_table = create_freq_table(my_data)
    priority_list = create_priority_list(my_data, freq_table)
    encode_table = create_encode_table(my_data, priority_list)
    return(encode(my_data,encode_table))


'''
    Function which gets an encoder table and returns a format you can print on screen
'''


def encoder2txt(encoder_table):
    result = ''
    for symbol in encoder_table.keys():
        if symbol == ' ':
            result += ('space: '+encoder_table[symbol]+'\n')
        else:
            result += (symbol +': '+encoder_table[symbol]+'\n')
    return result

