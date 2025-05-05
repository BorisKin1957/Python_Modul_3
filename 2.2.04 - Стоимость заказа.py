'''Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина.
В нем каждая строка с помощью символа табуляции \t разделена на три колонки:

наименование товара;
количество товара (целое число);
цена (в рублях) товара за 1 шт. (целое число).
Напишите программу, подсчитывающую общую стоимость заказа.

Sample Output:

1650'''

with open('TEXTs/prices.txt', 'r', encoding='utf-8') as file:
    total = []
    for line in file:
        line = line.strip()
        line = line.split('\t')
        total.append(int(line[1]) * int(line[2]))
    print(sum(total))