import csv
from datetime import datetime

lines = []
csv.register_dialect('my_dialect', delimiter=',', lineterminator="\n")
with (open("TEXTs\\dates_arrival.txt", 'r' , encoding='utf-8') as r_file1,
      open("TEXTs\\dates_departure.txt", 'r' , encoding='utf-8') as r_file2,
      open('TEXTs\\result.csv', 'w' , encoding='utf-8') as w_file):
    lines.append('Дата прилета,Дата убытия,Количество дней')
    # file_writer = csv.writer(w_file, 'my_dialect')
    # file_writer.writerow(['Дата прилета','Дата убытия','Количество дней'])
    for row1, row2 in zip(csv.reader(r_file1), csv.reader(r_file2)):
        date_start = datetime.strptime(row1[0], '%d-%m-%y')
        date_end = datetime.strptime(row2[0], '%d-%m-%y')
        lines.append(f'{row1[0]},{row2[0]},{(date_end - date_start).days}')
        #file_writer.writerow([row1[0], row2[0], (date_end - date_start).days])
    w_file.write('\n'.join(lines))

with open("TEXTs\\result.csv", 'r' , encoding='utf-8') as file:
    print(*[line.replace(',', '\t') for line in file])