from optimal_merge import multi_merge



def make_encoded_bin_msg(string):
    string_as_list = list(string)
    encoded_msg = ""
    for index, char in enumerate(string_as_list):
        string_as_list[index] = format((ord(char)), '08b')
    encoded_msg = encoded_msg.join(string_as_list)
    print(encoded_msg)
    return encoded_msg

def get_msg_bin_size(string):
    msg_size = len(make_encoded_bin_msg(string))
    print(msg_size)
    return msg_size

def get_msg_bin_dictionary(string):
    encoding_dictionary = {}
    for index, char in enumerate(string):
        encoding_dictionary[char] = format((ord(char)), '08b')
    print(encoding_dictionary)
    return encoding_dictionary

make_encoded_bin_msg("Hello")
get_msg_bin_size("Hello")
get_msg_bin_dictionary("Hello")

def get_dict_of_char_counts(string):
    string_as_list = list(string)
    unique_chars_in_list = set(string_as_list)
    encoded_msg = ""
    number_of_chars = {}

    for char in unique_chars_in_list:
        number_of_chars[char] = string_as_list.count(char) 
    encoding_dictionary = {}
    print(number_of_chars)
    return(number_of_chars)

get_dict_of_char_counts("Hello")

def make_encoded_huffman_dict(string):
    number_of_chars = get_dict_of_char_counts(string)
    sorted_by_char_count = sorted(number_of_chars, key=lambda k: number_of_chars[k])
    #TODO: Make a dict of huffman 

    
    print(sorted_by_char_count)

make_encoded_huffman_dict("Hello there")

def make_encoded_huffman_msg(string):
    #TODO make the msg using the dictionary
    pass
        
# At the end, need to see the size