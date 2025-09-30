from src.models.token import Token
from array import array


def tokenize_infix(expr: str) -> list[Token]:
    expr = expr.replace(' ', '')  # remove spaces
    tokens = []
    state = 'START'
    current_token = ''

    for char in expr:

        if state == 'START':
            if char.isdigit():
                state = 'NUMBER'
                current_token = char
            elif char == '+':
                tokens.append(Token('PLUS', char, 1))
            elif char == '-':
                tokens.append(Token('MINUS', char, 1))
            elif char == '*':
                state = 'MUL'
            elif char == '/':
                state = 'DIV'
            elif char == '%':
                tokens.append(Token('MOD', char, 2))
            elif char == '(':
                tokens.append(Token('LEFT', char, 3))
            elif char == ')':
                tokens.append(Token('RIGHT', char, 3))
            elif char == '.':
                state = 'FLOAT'
                current_token = '0.'
            elif char == '~':
                current_token += '-'
                state = 'NUMBER'
            else:
                raise ValueError(f'Неверный символ: {char}')

        elif state == 'NUMBER' or state == 'FLOAT':
            if char.isdigit():
                current_token += char
            elif char == '.':
                current_token += char
            else:
                tokens.append(Token('NUMBER', current_token, 0))
                current_token = ''
                # повторно обрабатываем текущий символ
                if char == '+':
                    tokens.append(Token('PLUS', char, 1))
                    state = 'START'
                elif char == '-':
                    tokens.append(Token('MINUS', char, 1))
                    state = 'START'
                elif char == '*':
                    state = 'MUL'
                elif char == '/':
                    state = 'DIV'
                elif char == '%':
                    tokens.append(Token('MOD', char, 2))
                    state = 'START'
                elif char == '(':
                    tokens.append(Token('LEFT', char, 3))
                    state = 'START'
                elif char == ')':
                    tokens.append(Token('RIGHT', char, 3))
                    state = 'START'
                else:
                    raise ValueError(f'Неверный символ: {char}')

        elif state == 'MUL':
            if char == '*':
                tokens.append(Token('POW', '**', 3))
                state = 'START'
            else:
                tokens.append(Token('MUL', '*', 2))
                # повторно обрабатываем текущий символ
                if char.isdigit():
                    state = 'NUMBER'
                    current_token = char
                else:
                    state = 'START'
                    if char == '+':
                        tokens.append(Token('PLUS', char, 1))
                    elif char == '-':
                        tokens.append(Token('MINUS', char, 1))
                    elif char == '/':
                        state = 'DIV'
                    elif char == '%':
                        tokens.append(Token('MOD', char, 2))
                    elif char == '(':
                        tokens.append(Token('LEFT', char, 3))
                    elif char == ')':
                        tokens.append(Token('RIGHT', char, 3))
                    else:
                        raise ValueError(f'Неверный символ: {char}')

        elif state == 'DIV':
            if char == '/':
                tokens.append(Token('FLOORDIV', '//', 2))
                state = 'START'
            else:
                tokens.append(Token('DIV', '/', 2))
                # повторно обрабатываем текущий символ
                if char.isdigit():
                    state = 'NUMBER'
                    current_token = char
                else:
                    state = 'START'
                    if char == '+':
                        tokens.append(Token('PLUS', char, 1))
                    elif char == '-':
                        tokens.append(Token('MINUS', char, 1))
                    elif char == '*':
                        state = 'MUL'
                    elif char == '%':
                        tokens.append(Token('MOD', char, 2))
                    elif char == '(':
                        tokens.append(Token('LEFT', char, 3))
                    elif char == ')':
                        tokens.append(Token('RIGHT', char, 3))
                    else:
                        raise ValueError(f'Неверный символ: {char}')

    if state == 'NUMBER':
        tokens.append(Token('NUMBER', current_token, 0))

    return tokens
