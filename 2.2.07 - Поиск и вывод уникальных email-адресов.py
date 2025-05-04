import re

emails = []

with open('emails.txt', 'r', encoding='utf-8') as file:
    #regex = r'(?i)(?:[a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9]+(?:\.[a-z0-9]+)+'
    regex = r'(?i)[a-z0-9_-]+@[a-z0-9]+\.[a-z0-9]+'
    for line in file:
        email = re.findall(regex, line)
        emails.extend(email)
    result = set(emails)
    print(f'Количество уникальных email-адресов:\n{len(result)}')
    print('Список уникальных email-адресов:')Работа с текстовыми и бинарными файлами
    print(*sorted(result), sep='\n')