def word_count(text):
    split_words = text.split()
    word_counter = 0
    for n in split_words:
        word_counter+=1
    return word_counter



def count_letter(text_string):
    convert_to_lower_case = text_string.lower()
    new_dict = {}

    for letter in convert_to_lower_case:
       if letter not in new_dict:
           new_dict[letter] = 1
       else:
           new_dict[letter]+=1

    return new_dict



def sort_dict(dict):

    sorted_dict = []

    for val in dict:
        new_dict = {}
        new_dict["char"] = val
        new_dict["num"] = dict[val]
        sorted_dict.append(new_dict)

    def sort_on(items):
        return items["num"]

    sorted_dict.sort(reverse=True,key=sort_on)

    sort_list = []

    for val in sorted_dict:
        sort_list.append(val)

    return sort_list