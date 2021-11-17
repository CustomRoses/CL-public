#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Luc Aggett, Natalia Haesler
# date: 03.11.2021

# TASK 2



# I misread the task at first, this is a function that accomplishes the task without a for loop
def not_for():
    x = input("Enter a word: ").lower()
    if x == x[::-1]:
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")


# the version with a for loop
def with_for():
    x = input("Enter a word: ").lower()
    xreverse = ""
    # reverse the string
    for letter in x:
        xreverse = letter + xreverse
    if xreverse == x:
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")


if __name__ == '__main__':
    not_for()
    with_for()
