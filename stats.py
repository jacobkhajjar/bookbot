def count_words(text):
    list = text.split()
    return len(list)


def count_characters(text):
    dictionary = {}
    lowered = text.lower()
    for char in lowered:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary


def sort_characters(dict_unsorted):
    list_char = []
    for k in dict_unsorted:
        if k.isalpha():
            dict_temp = {"char": k, "num": dict_unsorted[k]}
            list_char.append(dict_temp)
    def sort_by(dict):
        return dict["num"]
    list_char.sort(reverse=True, key=sort_by)
    return list_char