def solve_quadratic_equation(a, b, c):
    """Решение квадратного уравнения"""
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return f'Корни не существуют'
    # elif d == 0:
    #     x = (-b) / (2 * a)
    #     return f'{x} (единственный корень уравнения)'
    else:
        x1 = (-b + (d ** (1 / 2))) / (2 * a)
        x2 = (-b - (d ** (1 / 2))) / (2 * a)
    return x1, x2
