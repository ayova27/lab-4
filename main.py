def task_1():
    """Эта функция запрашивает у пользователя строку и сохраняет ее в переменной user_input.
Затем она преобразует строку в кортеж, называемый turtles, где каждый символ строки становится отдельным элементом кортежа.
Наконец, функция выводит кортеж turtles."""
    user_input = str(input("String or number: "))
    turtles = tuple(user_input)

    print(turtles)


# task_1()


def task_2():
    """В этой функции есть заранее заданный кортеж dauletsuper, содержащий символы.
Функция инициализирует пустую строку string.
Она перебирает каждый элемент в dauletsuper и добавляет их к строке string.
По завершении цикла функция выводит строку string."""
    dauletsuper = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')

    string = ''

    for i in dauletsuper:
        string += i

    print(string)


# task_2()


def task_3():
    """Эта функция определяет два кортежа: tuple_a и tuple_b.
Она вычисляет индекс, разделив длину кортежа tuple_b пополам.
Затем она создает новый кортеж tuple_c, объединяя первую половину tuple_a и вторую половину tuple_b.
Функция выводит tuple_c."""
    tuple_a = (1, 2, 3, 4, 5, 6, 7)
    tuple_b = (5, 6, 7, 9, 7, 1, 10, 10)

    index = len(tuple_b) // 2

    tuple_c = tuple_a[:index] + tuple_b[index:]

    print(tuple_c)


# task_3()


def task_4():
    """Эта функция инициализирует пустой список tuple_a.
Она запрашивает у пользователя строку с числами, разделенными запятыми, разбивает ввод и добавляет элементы в tuple_a.
Затем она создает новый список dauletsuper для хранения уникальных элементов и их количества.
Функция перебирает tuple_a, подсчитывает количество вхождений каждого элемента и добавляет список с элементом и его количеством в dauletsuper.
В конце функция преобразует dauletsuper в кортеж и выводит его."""
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
    """Функция принимает строку пользователя, содержащую числа или строки, разделенные запятыми, и разбивает ее.
Она классифицирует элементы в три отдельных списка: strings (не числовые строки), integers (целые числа) и floats (числа с плавающей запятой).
Затем она выводит эти три списка."""
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
    """
    Эта функция запрашивает у пользователя строку и преобразует ее в множество sets.
Затем она выводит множество sets.
    :return:
    """
    user_input = input("Object: ")
    sets = {str(x) for x in user_input}
    print(sets)


# task_2_1()

def task_2_2():
    """Функция принимает ввод пользователя для двух множеств, разделяет их и преобразует во множества set_a и set_b.
Она вычисляет симметрическую разницу между этими множествами и сохраняет результат в set_c.
Затем она выводит set_c."""
    user_input_a = input("Set a:").split(",")
    user_input_b = input("Set b:").split(",")

    set_a = {int(x) for x in user_input_a}
    set_b = {int(x) for x in user_input_b}

    set_c = set_a ^ set_b

    print(set_c)


# task_2_2()

def task_2_3():
    """Эта функция похожа на task_2_2, но вычисляет разницу множеств (вычитание) между set_b и set_a и сохраняет результат в set_c.
Затем она выводит set_c."""
    user_input_a = input("Set a:").split(",")
    user_input_b = input("Set b:").split(",")

    set_a = {int(x) for x in user_input_a}
    set_b = {int(x) for x in user_input_b}

    set_c = set_b - set_a

    print(set_c)


# task_2_3()

def task_2_4():
    """Функция принимает три множества и выполняет ряд операций с множествами.
Она копирует set_c в is_copy_set_c и перебирает его элементы. Если элемент найден в set_a, он удаляется из set_a и добавляется в set_b.
В конце функция выводит обновленные set_a, set_b и объединение set_c и set_b."""
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
    """Эта функция создает список списков. Она запрашивает у пользователя размер списков и количество элементов в каждом списке.
Она использует множество set_a в качестве источника элементов и многократно выбирает случайные элементы для создания подсписков.
Эти подсписки добавляются в основной список до достижения желаемого размера.
Затем она выводит получившийся список списков."""
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
    """
    Эта функция принимает ввод пользователя в виде строки, представляющей список кортежей, где каждый кортеж содержит марку и название.
Она обрабатывает ввод, чтобы преобразовать его в список кортежей и сохраняет его в переменной tuples.
Затем она перебирает эти кортежи и организует данные, подсчитывая частоту марок и сохраняя соответствующие названия.
Результат хранится в списке dauletsuper, который содержит марку, количество и связанные названия.
Функция выводит dauletsuper.
    """
    # (‘BMW’, ‘X6’), (‘Toyota’, ‘Yaris’), (‘Fiat’, ‘500’), (‘Fiat’, ‘Panda’), (‘Toyota’, ‘Camry 30’)
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
    """
    Эта функция похожа на task_4(), но с дополнительным функционалом. Она запрашивает у пользователя список чисел, разделяет его и сохраняет в tuple_a.
Она создает список remus для хранения уникальных элементов и их количества.
Также функция определяет самое необычное и популярное число и выводит их на экран с помощью алгоритма сортировки выбором.
С помощью быстрый сортировки было бы быстрее O(n log n), но сортировка выбором легче O(n^2).
    """
    # 5, 55, 10, 1, 0, 1, 55, 77, 10, 5, 5, 55, 77
    tuple_a = []

    input_string = input("Числа: ").split(', ')
    tuple_a += input_string

    remus = []

    for i in tuple_a:
        index = tuple_a.count(i)
        if (i, index) not in remus:
            i = int(i)
            remus.append([i, index])

    def selection_sort(romulus):
        for x in range(len(romulus)):
            lowest_index = x
            for numbers in range(x + 1, len(romulus)):
                if romulus[numbers][1] < romulus[lowest_index][1]:
                    lowest_index = numbers
            romulus[x], romulus[lowest_index] = romulus[lowest_index], romulus[x]

    selection_sort(remus)

    duplicate_remus = []
    for item in remus:
        if item not in duplicate_remus:
            duplicate_remus.append(item)

    tuple_c = tuple(duplicate_remus)
    print(tuple_c)

    print(f"\nThe most unusual number is {duplicate_remus[0]}\nThe most popular number is {duplicate_remus[-1]}")


task_bonus()
