# lesson7

# Задание №1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

from random import shuffle, randint


def create_and_shuffle():
    while True:
        try:
            m = int(input('\nВведите длину одномерного массива: '))
            break
        except ValueError:
            print('Вы ввели не венрое значение. Должно быть целое положительне число')

    array = [randint(-100, 100) for i in range(m)]
    shuffle(array)
    return array


def bubble_sort(array):
    ln = len(array) - 1

    ticket = True

    while ticket:
        ticket = False

        for i in range(0, ln):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            ticket = True
        ln -= 1

    return array


def main_func():
    array = create_and_shuffle()

    print('*' * 60)
    print('Сортировка массива в обратном порядке методом пузырька')
    print('*' * 60)
    print('Исходный массив имеет вид:\n', array)
    print('*' * 60)
    print('Отсортированный список:\n', bubble_sort(array))
    print('*' * 60)


main_func()
