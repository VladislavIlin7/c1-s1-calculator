from src.models.token import Token
from array import array



def calculate(tokens: array[Token]) -> float:
    stack = []

    for token in tokens:

        if token.type == 'NUMBER':
            stack.append(token)

        elif token.type == 'PLUS':
            a = stack.pop()
            b = stack.pop()
            stack.append(Token('NUMBER', float(a.value) + float(b.value), 0))

        elif token.type == 'MINUS':
            a = stack.pop()
            b = stack.pop()
            stack.append(Token('NUMBER', float(b.value) - float(a.value), 0))

        elif token.type == 'DIV':
            a = stack.pop()
            b = stack.pop()
            stack.append(Token('NUMBER', float(b.value) / float(a.value), 0))

        elif token.type == 'MUL':
            a = stack.pop()
            b = stack.pop()
            stack.append(Token('NUMBER', float(a.value) * float(b.value), 0))

    return stack[0].value