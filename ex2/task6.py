def task6():
    #
    # state here what your program does:
    #
    # input: a number (usrinput) and a character (char)
    # output: printed lines on the consoles in the shape of a diamond with a height of usrinput*2, made of the
    # character char with the word "shine" in the middle if the size of the diamond is larger than
    #

    # this portion of the code initialises the variables that are required for the printing to function
    usrinput = input('Please enter desired height of the diamond: ')  # gets the user input
    char = input('Which character should be used? ')  # gets the character to be used

    var1 = int(usrinput)
    var2 = var1 * 2 - 1

    varA = 0  # varA - var1 =
    varB = 1  # holds the number of characters that need to be printed on the current line
    varC = 0  #
    # this marks the beginning of our printed pattern, by adding a new line
    print("\n----------------------------\n")

    while (varA < var1):
        if (var1 - varA) < var1 / 2:
            varC += 2
            print(varA, varB, varC)
            if var1 - varA == 1 and varC >= 8:
                # this if statements add the word "SHINE" if the diamond is sufficiently large
                # and we are in the middle of the diamond.
                varD = int((varC - 5) / 2)
                print(" " * int((var2 - varB) / 2) + char * int(
                    varB / 2 - varC / 2) + varD * " " + "SHINE" + varD * " " + char * int(varB / 2 - varC / 2 + 2))
            else:
                print(varA, varB, varC)
                print(" " * int((var2 - varB) / 2)  # print whitespace
                      + char * int(varB / 2 - varC / 2) + varC * " "  # print character, then whitespace
                      + char * int(varB / 2 - varC / 2 + 1))  # print character after whitespace
        else:
            print(" " * int((var2 - varB) / 2) + char * varB)
            # print the correct amount of whitespace, then our character
        varA += 1 # update values for to make more whitespace and more characters
        varB += 2

    varA -= 1 #update values for less whitespace and less characters
    varB -= 2

    while (varA >= 0): #prints the smaller part of the diamond, decreasing the size over time until we reach the end.
        if (var1 - varA) < var1 / 2:
            varC -= 2
            print(" " * int((var2 - varB) / 2) + char * int(varB / 2 - varC / 2) + varC * " " + char * int(
                varB / 2 - varC / 2 + 1))
        else:
            print(" " * int((var2 - varB) / 2) + char * varB)
        varA -= 1
        varB -= 2

    print("\n----------------------------\n")


if __name__ == "__main__":
    task6()
