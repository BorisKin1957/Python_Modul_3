'''Описание задания: В данном задании вам необходимо проанализировать данные из
 CSV файла(credit_train.csv), находящегося в текущей директории и выполнить следующие действия:

Выведите названия всех столбцов в отсортированном порядке.
Найдите максимальное, минимальное и среднее значение в столбце "Current Credit Balance".
Округлите все величины до целого значения
Для самостоятельного тестирования своего алгоритма вы можете скачать файл credit_train.csv.

Примечание: Выполнение задания может быть осуществлено с помощью библиотеки csv .
Подумайте о том, как вы будете читать
данные из файла и анализировать их с помощью этой библиотеки.'''

import csv

lst, n = [], 0

with open('TEXTs\\credit_train_all.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        if n == 0:
            column, n = row.index('Current Credit Balance'), 1
            print(*sorted(row), sep='\n')
            continue
        lst.append(float(row[column]))

    print(int(max(lst)), int(min(lst)), int(sum(lst) / len(lst)), sep='\n')