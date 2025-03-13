def word_count(text):
    return len(text.split())

def char_dict(text):
    char_dict = {}

    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict

def sort_dict(dict):
    dict_list = []

    def sort_on_count(dict):
        return dict["count"]
    
    for key, value in dict.items():
        new_dict = {"name": f"{key}", "count": value}
        dict_list.append(new_dict)

    dict_list.sort(reverse= True, key=sort_on_count)
    return dict_list

def print_report(filepath, words, list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for dict in list:
        if dict['name'].isalpha():
            print(f"{dict['name']}: {dict['count']}")

    

        