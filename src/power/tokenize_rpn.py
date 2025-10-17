from src.models.token import Token
from array import array


def tokenize_rpn(expr: str) -> list[Token]:
    """Splits the entered expression in postfix notation into tokens"""
    expr_split = expr.replace('(', '').replace(')', '').split()
    tokens = []

    for part in expr_split:
        part = part.replace('~', '-')
        if part[0] == '-' and len(part) > 1 and part[1:].isdigit():
            tokens.append(Token('NUMBER', part, 0))
        elif part[0] == '+' and len(part) > 1 and part[1:].isdigit():
            tokens.append(Token('NUMBER', part[1:], 0))
        elif '.' in part and part.count('.') == 1:
            parts = part.split('.')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
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
        elif part == '**':
            tokens.append(Token('POW', part, 3))
        elif part == '//':
            tokens.append(Token('FLOORDIV', part, 2))
        elif part == '%':
            tokens.append(Token('MOD', part, 2))
        else:
            raise TypeError(f'Неверный символ - {part}')

    return tokens
