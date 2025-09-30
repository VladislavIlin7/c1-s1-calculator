from src.models.token import Token
from array import array


def convert_infix_to_rpn(tokens: array[Token]) -> array[Token]:
    output = []
    stack = []

    for token in tokens:
        if token.type_token == 'NUMBER':
            output.append(token)
        elif token.type_token in ['PLUS', 'MINUS', 'MUL', 'DIV', 'POW', 'MOD', 'FLOORDIV']:
            while (stack and stack[-1].type_token in ['PLUS', 'MINUS', 'MUL', 'DIV', 'POW', 'MOD', 'FLOORDIV']
                   and stack[-1].priority >= token.priority):
                output.append(stack.pop())
            stack.append(token)
        elif token.type_token == 'LEFT':
            stack.append(token)
        elif token.type_token == 'RIGHT':
            while stack and stack[-1].type_token != 'LEFT':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())

    return output
