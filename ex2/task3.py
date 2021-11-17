def task3():
    fn = input("Enter first name:")
    ln = input("Enter last name:")
    city = input("Enter City")
    if len(fn) <= len(city):
        print(fn.lower(), ln.upper(), city.lower())
    else:
        print(fn.upper(), ln.lower(), city.upper())


if __name__ == "__main__":
    task3()
