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


# task_2_1()

def task_2_2():
    user_input_a = input("Set a:").split(",")
    user_input_b = input("Set b:").split(",")

    set_a = {int(x) for x in user_input_a}
    set_b = {int(x) for x in user_input_b}

    set_c = set_a ^ set_b

    print(set_c)


# task_2_2()

def task_2_3():
    user_input_a = input("Set a:").split(",")
    user_input_b = input("Set b:").split(",")

    set_a = {int(x) for x in user_input_a}
    set_b = {int(x) for x in user_input_b}

    set_c = set_b - set_a

    print(set_c)


# task_2_3()

def task_2_4():
    user_input_a = input("Set a:").split(", ")
    user_input_b = input("Set b:").split(", ")
    user_input_c = input("Set c:").split(", ")

    set_a = {int(x) for x in user_input_a}
    set_b = {int(x) for x in user_input_b}
    set_c = {int(x) for x in user_input_c}

    is_copy_set_c = set_c.copy()

    for i in is_copy_set_c:
        if i in set_a:
            set_a.remove(i)
            set_b.add(i)

    print("Updated set_a:", set_a)
    print("Updated set_b:", set_b)
    print("Updated set_c:", set_c | set_b)


# task_2_4()

def task_2_5():
    import random

    input_list_size = int(input("Size: "))
    input_quality = int(input("Quantity: "))

    set_a = {1, 2, 3, 4, 5, 6}
    set_a_copy = list(set_a)
    lists = []

    while len(lists) < input_list_size:
        dauletsuper = []
        while len(dauletsuper) < input_quality + 1:
            x = random.choice(set_a_copy)
            if x not in dauletsuper:
                dauletsuper.append(x)
        if dauletsuper not in lists:
            lists.append(dauletsuper)

    for i in enumerate(lists, 1):
        print(i)


# task_2_5()


def task3():
    # input: (‘BMW’, ‘X6’), (‘Toyota’, ‘Yaris’), (‘Fiat’, ‘500’), (‘Fiat’, ‘Panda’), (‘Toyota’, ‘Camry 30’)
    user_input = input("Input: ").replace("‘", "'").replace("’", "'")

    tuples = eval(user_input)
    caesar = list(tuples)
    dauletsuper = []

    for brand, name in caesar:
        found = False
        for i in range(0, len(dauletsuper), 3):
            if dauletsuper[i] == brand:
                dauletsuper[i + 1] += 1
                found = True
                if name not in dauletsuper[i + 2]:
                    dauletsuper[i + 2].append(name)
                break
        if not found:
            dauletsuper.extend([brand, 1, [name]])

    print(dauletsuper)


# task3()


def task_bonus():
    # 5, 55, 10, 1, 0, 1, 55, 77, 10, 5, 5, 55, 77
    tuple_a = []

    input_string = input("Numbers: ").split(', ')
    tuple_a += input_string

    dauletsuper = []

    for i in tuple_a:
        index = tuple_a.count(i)
        if (i, index) not in dauletsuper:
            i = int(i)
            dauletsuper.append([i, index])

    for x in range(len(dauletsuper)):
        lowest_index = x
        for numbers in range(x + 1, len(dauletsuper)):
            if dauletsuper[numbers][-1] < dauletsuper[lowest_index][-1]:
                lowest_index = numbers
        dauletsuper[x], dauletsuper[lowest_index] = dauletsuper[lowest_index], dauletsuper[x]

    tuple_c = tuple(dauletsuper)

    print(tuple_c)

task_bonus()
