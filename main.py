def task_1():
    user_input = str(input("String or number: "))
    turtles = tuple(user_input)

    print(turtles)


# task_1()


def task_2():
    dauletsuper = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')

    string = ''

    for i in dauletsuper:
        string += i

    print(string)


# task_2()


def task_3():
    tuple_a = (1, 2, 3, 4, 5, 6, 7)
    tuple_b = (5, 6, 7, 9, 7, 1, 10, 10)

    index = len(tuple_b) // 2

    tuple_c = tuple_a[:index] + tuple_b[index:]

    print(tuple_c)


# task_3()


def task_4():
    import sys
    tuple_a = tuple()

    for tuples in sys.stdin:
        tuples.split(",")
        tuple_a = str(tuples)

    index = 0
    tuple_c = tuple()
    dauletsuper = []

    for i in tuple_a:
        while len(tuple_a):
            if i in tuple_a[index]:
                index += 1
                tuple_c += (i, index)
                continue
            else:
                continue

    print(tuple_c)
task_4()
