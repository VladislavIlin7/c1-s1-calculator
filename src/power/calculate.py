from src.models.token import Token
from array import array


def calculate(tokens: array[Token]) -> float:
    stack = []
    for token in tokens:
        if token.type == 'NUMBER':
            stack.append(float(token.value))
        elif token.type == 'PLUS':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif token.type == 'MINUS':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif token.type == 'DIV':
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)
        elif token.type == 'MUL':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif token.type == 'POW':
            a = stack.pop()
            b = stack.pop()
            stack.append(b ** a)
        elif token.type == 'MOD':
            a = stack.pop()
            b = stack.pop()
            stack.append(b % a)
        elif token.type == 'FLOORDIV':
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
    return stack[0]