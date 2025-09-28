from src.models.token import Token
from array import array


def convert_infix_to_rpn(tokens: array[Token]) -> array[Token]:
    output = []
    stack = []

    for token in tokens:
        if token.type == 'NUMBER':  # операнд
            output.append(token)
        elif token.type in ['PLUS', 'MINUS', 'MUL', 'DIV']:  # оператор
            while stack and stack[-1].type in ['PLUS', 'MINUS', 'MUL', 'DIV'] and stack[-1].priority >= token.priority:
                output.append(stack.pop())
            stack.append(token)
        elif token.type == 'LEFT':
            stack.append(token)
        elif token.type == 'RIGHT':
            while stack and stack[-1].type != 'LEFT':
                output.append(stack.pop())
            stack.pop()  # убрать '('

    while stack:
        output.append(stack.pop())

    return output



