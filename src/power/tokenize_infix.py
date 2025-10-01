from src.models.token import Token


def tokenize_infix(expr: str) -> list[Token]:
    """Splits the entered expression in infix notation into tokens"""
    expr = expr.replace(' ', '').replace('**', '^').replace('//', '$')

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
                tokens.append(Token('MUL', char, 2))
            elif char == '/':
                tokens.append(Token('DIV', char, 2))
            elif char == '%':
                tokens.append(Token('MOD', char, 2))
            elif char == '^':
                tokens.append(Token('POW', char, 3))
            elif char == '$':
                tokens.append(Token('FLOORDIV', char, 2))
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
                raise ValueError(f'Неверный символ - {char}')

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
                    tokens.append(Token('MUL', char, 2))
                    state = 'START'
                elif char == '/':
                    tokens.append(Token('DIV', char, 2))
                    state = 'START'
                elif char == '^':
                    tokens.append(Token('POW', char, 3))
                    state = 'START'
                elif char == '$':
                    tokens.append(Token('FLOORDIV', char, 2))
                    state = 'START'
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
                    raise ValueError(f'Неверный символ - {char}')

    if state == 'NUMBER':
        tokens.append(Token('NUMBER', current_token, 0))

    return tokens
