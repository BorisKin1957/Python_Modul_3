'''Реализуйте функцию simulate_dice_throw, которая возвращает случайное целое число от 1 до 6,
имитируя бросок игральной кости.
Реализуйте функцию determine_winner(player1_result, player2_result),
которая принимает результаты бросков для двух игроков и определяет победителя.
Функция должна возвращать строку:
"Player 1", если первый игрок победил,
"Player 2", если второй игрок победил,
"It's a tie", если результаты бросков равны.
Внимание: Вам необходимо реализовать только функции. Тестирование будет проведено автоматически '''

import random

def simulate_dice_throw():
    return random.randint(1, 6)


def determine_winner(player1_result, player2_result):
    if player1_result > player2_result:
        return 'Player 1'
    elif player2_result > player1_result:
        return 'Player 2'
    return "It\'s a tie"

print(simulate_dice_throw())

print(determine_winner(simulate_dice_throw(), simulate_dice_throw()))

