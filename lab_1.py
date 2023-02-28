from itertools import groupby
from math import log


alphabet = str(input('Введите элементы словаря через запятую (например, a,b,c): ')).split(sep=',')
alphabet = [el for el, _ in groupby(alphabet)]
print(alphabet)

n = len(alphabet)

word = list(input('Введите слово: '))

k = len(word)

number = int(input('Введите число для преобразования в слово: '))
nums_arr = []


def make_num(len_word=k, num=0):
    global alphabet, n, word, k, nums_arr

    if len_word > 0:
        digit = alphabet.index(word[k - len_word]) + 1
        num += (n ** (len_word - 1)) * digit
        nums_arr.append([n ** (len_word - 1), digit])
        return make_num(len_word - 1, num)

    else:
        print(nums_arr)
        return num



def split_nums(array=None):
    global n, number

    if array is None:
        if number <= n:
            return [number]
        else:
            if number % n == 0:
                array = [(number // n) - 1, n, n]
            else:
                array = [number // n, n, number % n]

    def find_int(arr_left):
        if not (type(arr_left[0]) == int):
            return find_int(arr_left[0])
        else:
            return arr_left

    arr = find_int(array)

    def check_greater(arr):
        if arr[0] > n:
            return True
        else:
            return False

    if check_greater(arr):
        if arr[0] % n == 0:
            arr[0] = [(arr[0] // n) - 1, n, n]
        else:
            arr[0] = [arr[0] // n, n, arr[0] % n]
        return split_nums(array)
    else:
        return array


def make_degree(array):
    global n

    def move_to_left(ar_r):
        if not (type(ar_r[0][0]) == int):
            return move_to_left(ar_r[0])
        else:
            return ar_r

    arr = move_to_left(array)

    def change_arr(arr):
        first, last = arr.pop(0), [arr.pop(0), arr.pop(0)]

        for i in range(1, len(first), 2):
            first[i] *= n

        arr.extend(first + last)

    change_arr(arr)

    if type(array[0]) == int:
        return array
    else:
        return make_degree(array)


def decode(array):
    global n
    word_final = ''

    for i in range(1, len(array), 2):
        array[i] = int(log(array[i], n))

    for i in range(0, len(array), 2):
        word_final += str(alphabet[array[i] - 1])

    return word_final


print(f"Задание №1: Преобразование слова {word} в число =", make_num())

eq = split_nums()
print(f"Преобразование числа {number} в слово: \n{eq}")
print(make_degree(eq))
print(f"Итог преобразования: {decode(eq)}")
