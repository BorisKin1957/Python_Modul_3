'''Задание: Расчет возраста пользователя

Напишите функцию calculate_age(birth_date), которая принимает на вход дату рождения
пользователя в формате (год, месяц, день) и возвращает его возраст в полных годах.

Описание функции:

Функция calculate_age(birth_date) принимает на вход кортеж из трех элементов:
год, месяц и день. (birth_date=(year,month,day))
Функция должна корректно обрабатывать вводные данные, включая високосные года.
Возвращаемое значение функции должно быть целым числом, представляющим полный
возраст пользователя в годах.
 Реализуйте функцию calculate_age и убедитесь, что она работает корректно на
 различных входных данных.'''


from datetime import datetime

def test_calculate_age():
    # Тестовые входные данные и ожидаемые результаты
    test_cases = [
        ((2000, 1, 1), 25),  # Тест на возраст 25 лет
        ((1985, 12, 31), 39),  # Тест на возраст 39 лет
        ((2023, 6, 30), 1),  # Тест на возраст 1 год
        ((2010, 2, 28), 15),  # Тест на возраст 15 лет
        ((2012, 2, 29), 13)  # Тест на возраст 13 лет (високосный год)
    ]

    # Проверяем каждый тестовый случай
    for birth_date, expected_age in test_cases:
        # Вычисляем возраст
        age = calculate_age(birth_date)
        # Проверяем, что результат совпадает с ожидаемым
        assert age == expected_age, f"Ошибка: Для даты {birth_date} ожидается возраст {expected_age}, но получено {age}"

def calculate_age(birth_date: tuple) -> int:
    """
    Вычисляет возраст в годах на основе даты рождения.
    """
    birth_day = datetime(*birth_date)
    today = datetime.now()
    age = (today - birth_day).days // 365
    return age

# Запуск тестов
test_calculate_age()
print("Все тесты пройдены успешно!")


print(calculate_age((2000, 1, 1)))
print(calculate_age((1985, 12, 31)))
print(calculate_age((2023, 6, 30)))
print(calculate_age((2010, 2, 28)))
print(calculate_age((2012, 2, 29)))