from src.power import *


def print_usage():
    print('Выберите режим калькулятора:')
    print('     1-инфиксное')
    print('     2-постфиксное')
    print('     3-выход из программы')


def handle_input():
    mode: str = ''
    while mode != '3':
        print_usage()
        mode = input()
        if mode == '1':
            expr = input('Введите выражение в инфиксной форме:')
            print(f'Ответ: {calculate(convert_infix_to_rpn(tokenize_infix(expr)))}')
        elif mode == '2':
            expr = input('Введите выражение в постфиксной форме:')
            print(f'Ответ: {calculate(tokenize_rpn(expr))}')
        elif mode == '3':
            print('Пока Пока!')
        else:
            print(f'Неправильный ввод - {mode}')
            print('Попробуйте ещё раз')

handle_input()