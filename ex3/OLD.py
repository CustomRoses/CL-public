#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Luc Aggett, Natalia Haesler
# date: 03.11.2021
import re
import sys
from pprint import pprint

from nltk.corpus import stopwords




# This is the old version of the code, I still don't know why this doesn't properly remove stopwords. Feedback would be appreciated.



stopwords = set(stopwords.words("english"))  # use this set for removing the stopwords
with open('dune.txt') as book:
    context_left = {}
    context_right = {}
    for line in book:
        temp = line.lower()
        temp = re.sub("[.,;:/\-\n]", "", temp)
        temp = temp.split(" ")
        for word in temp:
            if word in stopwords:
                temp.remove(word)
        for word in temp:
            if word == "dune":
                for i in range(-2, 0):
                    # We need to check that there is actually words present at the position we're checking. Should there not be a word,
                    if temp.index("dune") + i < 0 or temp.index("dune") + i > len(temp) - 1:
                        continue
                    if not temp[temp.index("dune") + i] in context_left:
                        context_left.update({temp[temp.index("dune") + i]: [1]})
                    elif temp.index("dune") + i > 0:
                        context_left.get(temp[temp.index("dune") + i])[0] += 1
                for i in range(1, 3):
                    if temp.index("dune") + i > len(temp) - 1:
                        continue
                    if not temp[temp.index("dune") + i] in context_right:
                        context_right.update({temp[temp.index("dune") + i]: [1]})
                    elif temp.index("dune") + i > 0:
                        context_right.get(temp[temp.index("dune") + i])[0] += 1


# This block of code prints out our results,

context_right.pop("")
context_left.pop("")  # remove empty spaces that snuck in
print("Right Dictionary: ")
print(dict(sorted(context_right.items(), key=lambda item: item[1], reverse=True)))
print("\nLeft Dictionary:")
print(dict(sorted(context_left.items(), key=lambda item: item[1], reverse=True)))