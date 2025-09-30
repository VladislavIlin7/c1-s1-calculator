from src.models.token import Token
from array import array


def calculate(tokens: array[Token]) -> float:

    stack = []
    for token in tokens:

        if token.type_token == 'NUMBER':
            stack.append(float(token.value))
        elif token.type_token == 'PLUS':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif token.type_token == 'MINUS':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)

        elif token.type_token == 'DIV':
            a = stack.pop()
            b = stack.pop()
            if a==0:
                raise ZeroDivisionError('Деление на 0')
            else:
                stack.append(b / a)

        elif token.type_token == 'MUL':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif token.type_token == 'POW':
            a = stack.pop()
            b = stack.pop()
            stack.append(b ** a)
        elif token.type_token == 'MOD':
            a = stack.pop()
            b = stack.pop()
            stack.append(b % a)
        elif token.type_token == 'FLOORDIV':
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
    return stack[0]