from AnagramMakers import anagram_dictionary
import SpreadsheetGenerator


user_input = input("word: ").split(" ")
user_input_2 = input("How many times would you like the program to run?")

dict1 = {}
i = int(user_input_2)
j = 0
while j < i:
    dict1.update(anagram_dictionary(user_input))
    i -= 1
sorted_pairs = sorted(dict1.items())
arranged_pairs = (sorted(sorted_pairs, key=lambda anagrams: anagrams[1]))

SpreadsheetGenerator.spreadsheet_generator(arranged_pairs)
