import random


def anagram(word):
    dict1 = {}
    for ch in word:
        x = random.randint(0, 26)
        while x in dict1.keys():
            x = random.randint(0, 26)
        else:
            dict1.update({x: ch})

    x = sorted(dict1.items())
    y = list(zip(*x))
    (numbers, letters) = y
    output = ""
    for item in letters:
        output += item
    return output


def anagram_dictionary(words):
    list1 = list(words)
    dict2 = {anagram(x): x for x in list1}
    return dict2
