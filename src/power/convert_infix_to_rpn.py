from src.models import *
from src.power.bracketsException import BracketsException

def convert_infix_to_rpn(tokens: list[Token]) -> list[Token]:
    """Convert infix to postfix"""
    output = []
    stack = []

    for token in tokens:
        if token.type_token == 'NUMBER':
            output.append(token)
        elif token.type_token == 'UNARY_MINUS':
            stack.append(token)
        elif token.type_token in ['PLUS', 'MINUS', 'MUL', 'DIV', 'POW', 'MOD', 'FLOORDIV', 'UNARY_MINUS']:
            while (stack and stack[-1].type_token in ['PLUS', 'MINUS', 'MUL', 'DIV', 'POW', 'MOD', 'FLOORDIV', 'UNARY_MINUS']
                   and stack[-1].priority >= token.priority):
                output.append(stack.pop())
            stack.append(token)
        elif token.type_token == 'LEFT':
            stack.append(token)
        elif token.type_token == 'RIGHT':
            while stack and stack[-1].type_token != 'LEFT':
                output.append(stack.pop())
            if not stack:
                raise BracketsException('Неправильно расставлены скобки')
            stack.pop()
    for token in stack:
        if token.type_token == 'LEFT':
            raise BracketsException("Ошибка: не хватает закрывающей скобки ')'")
    while stack:
        output.append(stack.pop())

    final_output = []
    for token in output:
        if token.type_token == 'UNARY_MINUS':
            final_output.append(Token('NUMBER', '0', 0))
            final_output.append(Token('MINUS', '-', 1))
        else:
            final_output.append(token)

    return final_output
