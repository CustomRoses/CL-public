def word_count(text):
    """
    Counts the number of words in a given text and prints the result to the console.
    :return: None
    """
    count = 0
    for line in text:
        for word in line.split():
            count += 1
    print(count)


x = word_count("test")
print(x)
print(type(x))
# the function prints the result, but does not return it - it is a void function and will always return None.
