import os
##Assignment 1

jane = "The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever.  You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 ***START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE*** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."

jane_almost_cleaned = jane[jane.find('Produced'):]

jane_cleaned1 = jane_almost_cleaned.replace("man","person")
jane_cleaned = jane_cleaned1.replace("wife","partner")
print(jane_cleaned)

def swap_word_in_jane(oldword, newword):
    jane_cleaned_custom = jane_cleaned.replace(oldword,newword)
    print(jane_cleaned_custom)

swap_word_in_jane("Jane","Faadil")






