import sys


def checking(any_str, any_number):
    any_str = any_str.split()
    try:
        for i in range(len(any_str)):
            float(any_str[i])
        float(any_number)
    except TypeError:
        print("Ошибка. Значения введены некорректно. Закрытие программы.")
        sys.exit()


def changing(any_str):
    listed = []
    any_str = any_str.split()
    for i in range(len(any_str)):
        listed.append(float(any_str[i]))
    return listed


def sorting(any_list):
    for i in range(1, len(any_list)):
        index = i
        a = any_list[i]
        while index > 0 and any_list[index-1] > a:
            any_list[index] = any_list[index-1]
            index -= 1
        any_list[index] = a
    return any_list


def comparing(any_list, any_number):
    any_number, position = float(any_number), 0
    for i in range(0, len(any_list)):
        if any_list[i] >= any_number:
            position = i
            break
    if position - 1 < 0 or position == len(any_list):
        position = "Отсутствует. Число выходит за пределы последовательности"
    print(f"Ближайшая позиция в последовательности - {position}")


some_str = input("Введите последовательность чисел, отделяя каждое последующее одним пробелом: ")
some_number = input("Введите число, относительная позиция которого в последовательности будет определена: ")

checking(some_str, some_number)

comparing(sorting(changing(some_str)), some_number)
