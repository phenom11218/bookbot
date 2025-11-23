def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    lower_text = text.lower()

    character_counter = {}

    for char in lower_text:
        if char in character_counter:
            character_counter[char] += 1
        else:
            character_counter[char] = 1
        
    return(character_counter)


def get_sorted_list_dict(list):
    key_pair_list = []

    for char in list:
        key_pair_list.append({"char":char, "num":list[char]})
    
    key_pair_list.sort(reverse = True, key=sort_on)

    return key_pair_list

def sort_on(items):
    return items["num"] 
