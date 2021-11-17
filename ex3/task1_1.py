#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Luc Aggett, Natalia Haesler
# date: 03.11.2021

# TASK 1.1

# list of ingredients
from collections import Counter

painting = ['tree','cabine','mountain','tree','stone','mistake','waterfall','titanium white']

# TODO your implementation here


# Task A
print(dict((Counter(painting))).get("tree"))
# We use the builtin Counter Class here, which returns a Counter object which we cast to a dict,
# from which we can get the number of occurences of "tree"

# Task B
painting.pop(painting.index("tree", painting.index("tree") + 1))
# We get the second incidence of "tree" by finding the index of the first occurence of tree,
# then searching from 1 position later in the list.

# Task C
painting.insert(2, "bush")
# We use the builtin insert function

# Task D
print("the index of mountain is:", painting.index("mountain"))
# We use the builtin index function

# Task E
painting.append("signature")

# Task F
painting = ["happy little accidents" if w == "mistake" else w for w in painting]
# This is just a one-line way of writing the regular for-loop.

# Task G
print("the number of elements in painting is: ", len(painting))
# We can use len() to find the number of items.

# Task H
print("Here's your painting!\n", painting)

# Task i
mona_lisa = []

# Task J
mona_lisa.append(painting[3])

# Task K
mona_lisa.append("river")

# Task L
str = "mountain"
assert("mona lisa" == (str[0:2] + str[3] + str[5] + " lisa"))

# Task M
mona_lisa = sorted(mona_lisa)

mona_lisa.append("woman") # Have to add least add this
print("Here's our (slightly simplified) mona lisa", mona_lisa)