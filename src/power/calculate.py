from src.models import *
from src.power.modException import ModException
from src.power.manyOpsException import ManyOpsException
from src.power.manyArgsException import ManyArgsException
from src.power.floorDivException import FloorDivException



def calculate(tokens: list[Token]) -> float:
    """Evaluates an expression in postfix notation using the stack"""
    stack: list = []
    for token in tokens:
        if token.type_token == 'NUMBER':
            stack.append(float(token.value))
            continue

        if len(stack) < 2:
            raise ManyOpsException('Не верно введено выражение, недостаточно аргументов')

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
                raise ModException('MOD деление выполняется только с целыми числами')
            stack.append(b % a)
        elif token.type_token == 'FLOORDIV':
            if a == 0:
                raise ZeroDivisionError('Делить на 0 нельзя')
            if a != int(a) or b != int(b):
                raise FloorDivException('Целочисленное деление выполняется только с целыми числами')
            stack.append(b // a)

    if len(stack) > 1:
        raise ManyArgsException('Не верно введено выражение, много аргументов')
    return stack[0]
