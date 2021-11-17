#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Luc Aggett, Natalia Haesler
# date: 03.11.2021

import re
from nltk.corpus import stopwords

stopwords = list(stopwords.words("english"))  # use this set for removing the stopwords

with open('dune.txt') as text:
    context_left = {}
    context_right = {}
    book = text.read().lower()  # read the file and make the book lowercase
    book = re.sub("[.,;:/\-\n]", "", book)  # regular expression to remove all punctuation and newlines
    book = book.split(" ")  # convert book to list with split()
    for word in book:
        if word in stopwords:
            while word in book:
                print("\rcurrently removing: " + word + " | index: " + str(book.index(word)), end='', flush=True)
                book.remove(word)

    for i in range(0, len(book)): # This loop builds the context dictionaries
        if book[i] == "dune":
            for j in range(-2, 3):
                # Note: We used lists as the value, since their entries are easily changeable.
                # Branch: word not in left dictionary, create entry
                if j < 0 and not book[i + j] in context_left:
                    context_left.update({book[i + j]: [1]})
                # Branch: word in left dictionary, update value
                elif j < 0:
                    context_left.get(book[i + j])[0] += 1
                # Branch: word not in right dictionary, create entry
                if j > 0 and not book[i + j] in context_right:
                    context_right.update({book[i + j]: [1]})
                # Branch: word in right dictionary, update value
                elif j > 0:
                    context_right.get(book[i + j])[0] += 1





# This block print out the resulting context dictionaries
context_right.pop("")
context_left.pop("")  # remove empty strings

# Comment from Task 3 on this code:
# we create a new dictionary, taking advantage of the fact that we can get a list of tuples with the entries and keys
# in the dictionary using the items()  function. The key for the sorted function determines how the sort is done,
# so we provide a function that gives the sort function the second item of the tuple (word/number of occurences).

print("\nRight Dictionary: ")
print(dict(sorted(context_right.items(), key=lambda item: item[1], reverse=True)))
print("\nLeft Dictionary:")
print(dict(sorted(context_left.items(), key=lambda item: item[1], reverse=True)))