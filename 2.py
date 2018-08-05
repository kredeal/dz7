# lesson7

# Задание №2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


from random import uniform


def create_array():
    while True:
        try:
            m = int(input('\nВведите длину одномерного массива: '))
            break
        except ValueError:
            print('Вы ввели не венрое значение. Должно быть целое положительне число')

    array = [round(uniform(0, 50), 3) for i in range(m)]
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


def main_func():
    array = create_array()
    print('*' * 60)
    print('Сортировка массива методом слияния')
    print('*' * 60)
    print('Исходный список:\n', array)
    print('*' * 60)
    print('Отсортированный список:\n', merge_sort(array))
    print('*' * 60)


main_func()
