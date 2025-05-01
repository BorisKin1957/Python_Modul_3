'''Задание №1

Цель: Создать собственный модуль на языке программирования Python,
содержащий функцию для решения квадратного уравнения с использованием коэффициентов a, b и c.

Требования:

Создайте файл quadratic_solver.py, который будет содержать ваш собственный модуль.
В модуле должна быть функция solve_quadratic_equation(a, b, c),
принимающая три аргумента - коэффициенты квадратного уравнения.
Используйте формулу решения квадратного уравнения ax^2 + bx + c = 0:
Для действительных корней:
          x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)

          x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

Обработайте случаи отсутствия действительных корней.
В случае отсутствия действительных корней, верните сообщение:  Корни не существуют
Создайте файл 1.4.01 - Задание №1.py, в котором импортируйте ваш модуль и протестируйте функцию
solve_quadratic_equation для нескольких примеров квадратных уравнений.
Шаблон функции

def solve_quadratic_equation(a, b, c):
    pass
    return x1,x2
Пример использования на котором вы можете сами проверить свой модуль:

# 1.4.01 - Задание №1.py

from quadratic_solver import solve_quadratic_equation

# Тестирование
coefficients1 = (1, -3, 2)
coefficients2 = (1, 2, 1)
coefficients3 = (1, 1, 1)

result1 = solve_quadratic_equation(*coefficients1)
result2 = solve_quadratic_equation(*coefficients2)
result3 = solve_quadratic_equation(*coefficients3)

print(f"Уравнение {coefficients1}: Корни = {result1}")
print(f"Уравнение {coefficients2}: Корни = {result2}")
print(f"Уравнение {coefficients3}: Корни = {result3}")
Замечания:

Проверьте корректность работы вашего модуля, обрабатывая различные варианты
коэффициентов квадратного уравнения.
В файле 1.4.01 - Задание №1.py можно использовать различные примеры квадратных уравнений для
тестирования функции solve_quadratic_equation.
В "Редактор кода" представьте только код функции solve_quadratic_equation(a, b, c)
тестирование проведется автоматически.
Не забудьте написать импортирования необходимых стандартных библиотек,
если вы их используете в функции.'''

from mypackage.quadratic_solver import solve_quadratic_equation

# Тестирование
coefficients1 = (1, -3, 2)
coefficients2 = (1, 2, 1)
coefficients3 = (1, 1, 1)

result1 = solve_quadratic_equation(*coefficients1)
result2 = solve_quadratic_equation(*coefficients2)
result3 = solve_quadratic_equation(*coefficients3)

print(f"Уравнение {coefficients1}: Корни = {result1}")
print(f"Уравнение {coefficients2}: Корни = {result2}")
print(f"Уравнение {coefficients3}: Корни = {result3}")