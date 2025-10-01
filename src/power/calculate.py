from src.models.token import Token
from array import array


def calculate(tokens: array[Token]) -> float:
    """Evaluates an expression in postfix notation using the stack"""
    stack: array[float] = []
    for token in tokens:
        if token.type_token == 'NUMBER':
            stack.append(float(token.value))
            continue

        if len(stack) < 2:      # To calculate, you need at least 2 numbers in the stack
            raise SyntaxError('Не верно введено выражение, недостаточно аргументов')

        a = stack.pop()
        b = stack.pop()
        if token.type_token == 'PLUS':
            stack.append(a + b)
        elif token.type_token == 'MINUS':
            stack.append(b - a)
        elif token.type_token == 'DIV':
            if a == 0:
                raise ZeroDivisionError('Делить на 0 нельзя')
            stack.append(b / a)
        elif token.type_token == 'MUL':
            stack.append(a * b)
        elif token.type_token == 'POW':
            stack.append(b ** a)
        elif token.type_token == 'MOD':
            if a == 0:
                raise ZeroDivisionError('Делить на 0 нельзя')
            if a != int(a) or b != int(b):
                raise SyntaxError('MOD деление выполняется только с целыми числами')
            stack.append(b % a)
        elif token.type_token == 'FLOORDIV':
            if a == 0:
                raise ZeroDivisionError('Делить на 0 нельзя')
            if a != int(a) or b != int(b):
                raise SyntaxError('Целочисленное деление выполняется только с целыми числами')
            stack.append(b // a)

    if len(stack) > 1:
        raise SyntaxError('Не верно введено выражение, много аргументов')
    return stack[0]
