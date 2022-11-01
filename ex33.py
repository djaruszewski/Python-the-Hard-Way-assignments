i = 0
numbers = []

def ex33(x, y):
    i = 0
    numbers = []

    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

ex33(10, 2)

def ex34(x, y):
    i = 0
    numbers = []

    for i in range(0, x, y):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

ex34(10, 2)