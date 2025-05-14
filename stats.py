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