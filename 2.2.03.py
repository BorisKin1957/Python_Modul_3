'''Напишите программу, которая принимает от пользователя любое натуральное число N.
Затем программа записывает все числа от 1 до N в файл, каждое число на новой строке,
и выводит содержимое файла.

Для реализации программы используйте функции из предыдущего задания:
одну для записи в файл и другую для чтения содержимого файла.

Sample Input 1:

3
Sample Output 1:

1
2
3'''

def write_to_file(lst, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lst))


def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())

lst = [str(i) for i in range(1, int(input()) + 1)]

write_to_file(lst, 'expect.txt')
read_from_file('expect.txt')