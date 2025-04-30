'''Задание: Подсчет четных и нечетных чисел в списке

Напишите функцию count_even_odd, которая принимает на вход список из 100 случайных
целых чисел и возвращает количество четных и нечетных чисел в этом списке.

Описание функции:

Функция count_even_odd должна принимать на вход список из 100 случайных целых чисел.
Функция должна возвращать кортеж из двух элементов: количество четных чисел и
количество нечетных чисел в списке'''

import random


def count_even_odd(numbers: list[int]) -> tuple[int, int]:
    even = len([number for number in numbers if number % 2 == 0])
    odd = len([number for number in numbers if number % 2 != 0])
    return even, odd

# def count_even_odd(numbers: list[int]) -> tuple[int, int]:
#     even = len(list(filter(lambda x: x % 2 == 0, numbers)))
#     odd = len(list(filter(lambda x: x % 2 == 1, numbers)))
#     return even, odd
random_numbers = [random.randint(1, 100) for _ in range(100)]
print(type(random_numbers))
even_count, odd_count = count_even_odd(random_numbers)
print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)