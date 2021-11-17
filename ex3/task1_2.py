#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Luc Aggett, Natalia Haesler
# date: 03.11.2021

# TASK 1.2

# TODO your implementation here

# begin script

# definitions
list = []
counter = 0
while counter < 5:
    word = input("Enter any word")
    for char in word:
        # Iterate over every character in the word to check if it is alphanumeric
        if not char.isalpha():
            raise ValueError("Please enter a valid Input")
            # if the word does not fit our criteria, we raise an error
    if len(word) % 2 == 0:
        counter = -~counter
    # this one is kind of fun! this takes advantage of the fact that ~x == -x-1, so by taking -(~x) we get x+1
    list.append(word)

print(list.sort(key=len))
# we use the builtin sort function with the length of the word as our key