def task5():
    current_Word = "curr_word"
    last_Word = "last_word"
    length_total = 0
    input_count = 0
    while current_Word[0] is not last_Word[-1]:
        last_Word = current_Word
        current_Word = input(f" You've entered {length_total} characters so far. Please input your word:")
        length_total += len(current_Word)
        input_count += 1
    print(input_count)


if __name__ == "__main__":
    task5()
