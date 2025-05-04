'''Напишите две функции:

write_to_file(lst, filename): данная функция принимает список строк lst и
название файла filename. В теле функции осуществляется запись строк из списка
в файл с переданным именем. Будьте внимательны, в файле не должно быть пустой
последней строки.

read_from_file(filename): данная функция принимает имя файла filename и выводить
в консоль содержимое этого файла.

Пример списка для использования:

lst = ["John", "Oscar", "Jacob", "Emily", "Sophia", "Liam", "Emma"]'''


def write_to_file(lst, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lst))


def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())

lst = ["John", "Oscar", "Jacob", "Emily", "Sophia", "Liam", "Emma"]

write_to_file(lst, 'expect.txt')
read_from_file('expect.txt')
