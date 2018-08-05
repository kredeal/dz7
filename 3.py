# lesson7

# Задание №3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.


from random import randint


def create_array():
    while True:
        try:
            m = int(input('\nРазмер массива будет равен 2m+1. Введите значение m. m = '))
            break
        except ValueError:
            print('Вы ввели не венрое значение. Должно быть целое положительне число')

    array = [randint(-50, 50) for i in range(2 * m + 1)]
    return array


def merge_sort(array):
    array = array
    if len(array) <= 1:
        return array
    middle = int(len(array) / 2)
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]

        else:
            result.append(right[0])
            right = right[1:]

    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right

    return result


def counter(array):
    for i in array:

        k = 0
        l = 0

        for j in array:

            if i > j:
                k += 1
            if i < j:
                l += 1

        if k == l:
            return i


def main_func():
    array = create_array()

    print('*' * 40)
    print('Поиск медианы мессива')
    print('*' * 40)
    print('Исходный список: \n', array)
    print('*' * 40)
    print('Медианой массива является: \n', counter(array))
    print('*' * 40)
    print('Отсортированный список: \n', merge_sort(array))
    print('*' * 40)


main_func()
