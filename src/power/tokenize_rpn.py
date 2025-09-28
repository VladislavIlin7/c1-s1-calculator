from src.models.token import Token
from array import array

def tokenize_rpn(expr: str) -> array[Token]:
    expr_split = expr.replace('(', '').replace(')', '').split()
    tokens = []

    # 1+2 -> [1]
    for part in expr_split:
        part = part.replace('~', '-')
        if part[0] == '-' and len(part) > 1 and part[1:].isdigit():
            tokens.append(Token('NUMBER', part, 0))
        elif part.isdigit():
            tokens.append(Token('NUMBER', part, 0))
        elif part == '+':
            tokens.append(Token('PLUS', part, 1))
        elif part == '-':
            tokens.append(Token('MINUS', part, 1))
        elif part == '*':
            tokens.append(Token('MUL', part, 2))
        elif part == '/':
            tokens.append(Token('DIV', part, 2))
        else:
            raise 'Неверный символ'

    return tokens
