def task7():
    word = input("Please enter a word:")
    for i in range(len(word)):
        print(' '*(len(word) - i), word[i], ' ' * (i), word[i], ' ' * (i), word[i])


if __name__ == "__main__":
    task7()