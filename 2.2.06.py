'''Чтение данных тренировок из файла
Описание: В текущей директории находится текстовый файл train.txt,
содержащий данные о тренировках в формате "день, количество подтягиваний".
Напишите программу, которая позволит пользователю ввести номер дня,
а затем программа прочитает соответствующую строку из файла и выведет
запись о тренировке для этого дня.

Содержание файла train.txt:

Day 0, 8 pull ups
Day 1, 8 pull ups
Day 2, 9 pull ups
Day 3, 9 pull ups
Day 4, 9 pull ups
Day 5, 10 pull ups
Day 6, 10 pull ups
Day 7, 10 pull ups
Day 8, 10 pull ups
Day 9, 11 pull ups
Day 10, 11 pull ups
Day 11, 11 pull ups
Day 12, 11 pull ups
Day 13, 12 pull ups
Ввод: Пользователь вводит номер дня тренировки.

Вывод: Программа выводит запись о количестве подтягиваний выполненных в указанном день
в формате "Количество подтягиваний pull ups". Если такого номера дня нет в файле,
то должно вывестись сообщение No info'''

with open("prices.txt") as file:
    result = {}
    for line in file:
        line = line.strip()
        day_number, total = line.split(",")[0].split()[1], line.split(",")[1].split()[0]
        result[day_number] = int(total)

key = str(int(input()))
print(f'{result[key]} pull ups' if key in result else "No info")