from nltk.book import text1


def print_list_comprehension_results(text):

    # a) ALl words that end with ity and contain the letter 'b' but do not contain the letter 'm'
    outA = [
        word
        for word in text
        if word.endswith("ity") and "b" in word and "m" not in word
    ]
    print("a)", outA, "\nWords found:", len(outA))

    # b)  All words that start with u (case-insensitive) and are shorter than five characters.
    outB = [word for word in text if word.lower().startswith("u") and len(word) < 5]
    print("b)", outB, "\nWords found:", len(outB))

    # c) All words that contain the sequence of letters man, but do not start or end with it.
    outC = [
        word for word in text
        if "man" in word and not word.startswith("man") and not word.endswith("man")
    ]
    print("c)", outC, "\nWords found:", len(outC))

    # d)  All words with start with tan (case-sensitive) and do not have the letter g at the fourth position.
    outD = [word for word in text if word.startswith("tan") and word[3] != "g"]
    print("d)", outD, "\nWords found:", len(outD))

    # e)  All words containing at least three a and only one e.
    outE = [word for word in text if word.count("a") >= 3 and word.count("e") == 1]
    print("e)", outE, "\nWords found:", len(outE))

    return outA, outB, outC, outD, outE


print_list_comprehension_results(text1)
