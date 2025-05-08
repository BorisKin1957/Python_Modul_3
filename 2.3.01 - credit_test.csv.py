'''Вывод первых пяти значений столбца "Years in current job" из файла credit_test.csv
Описание задания: В этом задании требуется вывести первые пять значений столбца
"Years in current job" из файла credit_test.csv, который находится в текущей директории.

Для самостоятельного тестирования алгоритма можете использовать файл credit_train.csv.

Sample Output:

8 years
10+ years
8 years
3 years
5 years'''


import csv

n = 0

with open('TEXTs\\credit_train.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        if n == 0:
            n = 1
            column = row.index('Years in current job')
            continue
        if n <= 5:
            print(row[column])
        n += 1

