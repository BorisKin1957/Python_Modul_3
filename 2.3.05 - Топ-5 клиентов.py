'''Задача: Написать скрипт, который из файла credit_train.csv выберет 5 клиентов
с наибольшим годовым доходом Annual Income и запишет в файл result.csv таблицу c
4 столбцами по убыванию Annual Income:

годовым доходом Annual Income
статус кредита (Loan Status),
количество лет на текущей работе (Years in current job)
ежемесячные долговые обязательства (Monthly Debt).
Также выведите таблицу в терминал '''

import pandas as pd

# Чтение данных из файла CSV и создание DataFrame
df = pd.read_csv('TEXTs\\credit_train_all.csv')

# Сортировка DataFrame по столбцу 'Annual Income' в порядке убывания и выбор первых 5 строк
new_df = df.sort_values(by=['Annual Income'], ascending=False).head()

# Выбор определенных столбцов из DataFrame
new_df = new_df[['Annual Income', 'Loan Status', 'Years in current job', 'Monthly Debt']]

# Вывод DataFrame на экран без столбца с индексами строк
print(new_df.to_string(index=False))

# Запись данных DataFrame в файл CSV без индекса
new_df.to_csv('TEXTs\\result.csv', index=False)
