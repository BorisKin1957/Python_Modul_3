'''Определение места сильнейшего землетрясения
Вам необходимо разработать программу, которая выводит место (place) самого сильного
землетрясения по магнитуде (mag). Данные о землетрясениях хранятся в файле eq_data_1_day_m1.json,
расположенном в текущей директории.

Входные данные:
Файл eq_data_1_day_m1.json содержит информацию о землетрясениях в формате JSON.

Выходные данные:
Программа должна вывести место (place) самого сильного землетрясения по магнитуде (mag).'''

import json

with open('TEXTs\\eq_data_1_day_m1.json') as file:
    all_eq_data = json.load(file)

all_eq_dicts = all_eq_data['features']
all_eq_dicts = sorted(all_eq_dicts, key=lambda x: -x['properties']['mag'])

print(all_eq_dicts[0]['properties']['place'])
