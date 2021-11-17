#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Luc Aggett, Natalia Haesler
# date: 03.11.2021

# TASK 3

artists = {"Bob Ross": [1942, 1995], "Frida Kahlo": [1907, 1954], "Mary Cassatt": [1844, 1926],
           "Leonardo Davinci": [1452, 1519]}

artists.update({"Vincent van Gogh": [1852, 1890]})

# we first print the entry, followed by two tab characters, followed by the first part
# of the value tuple (the birth year), followed by the second entry in the tuple (the death year).
for entry in artists:
    print(entry + "\t\t" + str(artists.get(entry)[0]) + "-" + str(artists.get(entry)[1]))
input("\npress enter for next function\n")
# we create a new dictionary, taking advantage of the fact that we can get a list of tuples with the entries and keys
# in the dictionary using the items()  function. The key for the sorted function determines how the sort is done,
# so we provide a function that gives the sort function the second item of the tuple (the birth year/death year tuple).
# I was somewhat surprised to find that sorted() actually deals with this relatively well, simply sorting by the
# first element in the tuple.
for key in dict(sorted(artists.items(), key=lambda item: item[1], reverse=True)).keys():
    print(key)


# this raises an error, but the code runs. I'm still unsure why there is a TypeError here.

input("\npress enter for next function\n")

# a more readable & more easily understandable implementation of the above function:
def my_sort(item):
    return item[1]
# This function is used to sort the items. It swaps gets the second entry in the tuple, in this case
# the birthyear-deathyear tuple. This is needed for our sorting later.


artists = sorted(artists.items(), key=my_sort, reverse=True)
# We sort the list of artists using our my_sort function. we also reverse the list, since we want the largest number on top,
# and the default sort order is ascending. We want to sort by the items, since that's where the birthyears are saved.

artists = dict(artists)
# we have to turn our list of tuples into a dictionary again

for key in artists:
    print(key)
# print out the result