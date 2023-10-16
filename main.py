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
    tuple_a = []

    input_string = input("Numbers: ").split(', ')
    tuple_a += input_string

    dauletsuper = []

    for i in tuple_a:
        index = tuple_a.count(i)
        if (i, index) not in dauletsuper:
            dauletsuper.append([i, index])

    tuple_c = tuple(dauletsuper)

    print(tuple_c)


# task_4()

def task_5():
    # input = 55, 6, 777, 70.0, ‘7’, ‘A’
    caesar = []

    dauletsuper = input("Numbers or strings: ").split(", ")
    caesar.extend(dauletsuper)

    strings = []
    integers = []
    floats = []

    for i in caesar:
        i = i.strip()
        if i.isdigit():
            integers.append(int(i))
        elif i.replace(".", "").isdigit():
            floats.append(float(i))
        else:
            strings.append([i])

    print(f"{strings}\n{integers}\n{floats}")


# task_5()

def task_2_1():
    user_input = input("Object: ")
    sets = {str(x) for x in user_input}
    print(sets)

task_2_1()