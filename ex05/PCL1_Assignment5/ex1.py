import nltk.book
from nltk.book import text2


def subtask_a():
    """
    This expression creates a list with every word in text2 that is longer than 4 characters and shorter than 12,
    sorted alphabetically and converted to lowercase.
    """
    sorted([word.lower() for word in text2 if len(word) > 4 and len(word) < 12])


def subtask_b():
    text2 = 3
    # this raises a TypeError because the int type has no __len__ defined.

    text2 = [1, 2, 3]
    # this raises an AttributeError, because the int type has no lower() attribute.

    text2 = [[1, 2, 3, 4, 5, 6, 7], "winter_wren"]
    # this also raises an AttributeError, because the list type has no lower() attribute.


def subtask_c():
    out = []
    for word in text2:
        if 4 < len(word) < 12:
            out.append(word.lower())
    return sorted(out)


def subtask_d():
    text2 = set(nltk.book.text2)
    # this causes our book to be reduced to unique words, so if we ran the previous script over
    # the set we would get a list of unique words fulfilling the criteria specified above.
