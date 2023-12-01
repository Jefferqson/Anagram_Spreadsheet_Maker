# Anagram-Spreadsheet-Maker
Learning Project to make a program to randomize inputted words and output them in a spreadsheet. The goal was to get practice with Python and the openpyxl library.

The AnagramMakers.py file contains the anagram and anagram_dictionary functions. The first function takes a word and generates a dictionary with characters as the keys and assigns each a randomly generated, unique number. Then, the dictionary is sorted numerically the letters are taken out in their new order and put into an output string. The second function uses the first to allow the user to input any number of words.

main.py takes as input the words to be made into anagrams and the number of times that the program should run. It then alphabetizes them and pairs them with their original word.

It then calls the spreadsheet_generator function which takes the now-arranged pairs and enters them into an Excel spreadsheet with proper headings. 
