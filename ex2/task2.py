def task2():
    """
    Exercise 2: Text to number conversion \n
    This function calculates the results of the formulae given on the exercise sheets based on input from the user. \n
    does not return anything
    """
    a = input("Enter the value of variable a:")
    b = input("Enter the value of variable b:")
    try:
        float(a)
        float(b)
    except ValueError or TypeError:
        print("Please enter a valid number")
        return
    x = (3 * float(a) ** (4 / 5)) / (4 * (float(a) + float(b)))
    y = (x - float(a)) / 7 * float(b)
    print(f"Value of x: {x} \nValue of y: {y}")

    print(f"Value of x: {x}")
    print(f"Value of y: {y}")


if __name__ == "__main__":
    task2()
