def task4(word: str):
    if word.endswith(("er", "ismus")):
        return "der"
    elif word.endswith(("falt", "keit", "schaft", "ung")):
        return "die"
    elif word.endswith(("chen", "lein")):
        return "das"
    else:
        return "Gender could not be determined"


if __name__ == "__main__":
    task4("testchen")
