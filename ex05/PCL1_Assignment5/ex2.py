def subtask_a(text):
    """
    The code returns a list containing every non-consonant in the text, converted to uppercase.
    """

    non_consonants_list = []
    for char in text:
        if char not in [
            "b",
            "c",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "m",
            "n",
            "p",
            "q",
            "r",
            "s",
            "t",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]:
            non_consonants_list.append(char.upper())
    return non_consonants_list


converted_text = subtask_a("studying computational linguistics rocks!!")
print(converted_text)


def subtask_b(text):
    """
    this is an improved, faster-running version of the code above. it uses a set to store the non-consonants, which is faster in access than a list.
    it also converts the text to uppercase, which is faster than calling the upper() function on every single character.

    the function could also theoretically be made faster by inverting the condition (detecting vowels instead of non-consonants),
    but this would change the functionality, because non-consonants also include special characters, etc.
    """

    non_consonants_list = []
    text = text.upper()
    consonants = {
        "B",
        "C",
        "D",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    }
    for char in text:
        if char not in consonants:
            non_consonants_list.append(char)
    return non_consonants_list


converted_text = subtask_b("studying computational linguistics rocks!!")
print(converted_text)


def subtask_c():
    """
    there is no difference between output of the proposed code and the original.
    """
    assert subtask_a("studying computational linguistics rocks!!") == subtask_b(
        "studying computational linguistics rocks!!"
    )


def subtask_d(text):
    return [
        letter.upper()
        for letter in text.lower()
        if letter not in "bcdfghjklmnpqrstvwxyz"
    ]


print(subtask_d("studying computational linguistics rocks!!"))


def subtask_e(text):
    """
    This function can take a string, a list containing strings, a tuple containing strings, or a set containing strings.
    it can also take a dictionary with strings as keys and any data type as values, although this is not very useful.

    :param text:
    :return:
    """
    return [
        letter.upper()
        for letter in text
        if letter not in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    ]


print(subtask_e(["C", "L", "R", "O", "C", "K", "S"]))
print(subtask_e(("C", "L", "R", "O", "C", "K", "S")))
print(subtask_e({"C", "L", "R", "O", "C", "K", "S"}))
print(subtask_e({"C": 1, "L": 2, "R": 3, "O": 4, "K": 6, "S": 7}))
