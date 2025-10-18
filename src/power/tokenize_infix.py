from src.models.token import Token


def tokenize_infix(expr: str) -> list[Token]:
    """Splits the entered expression in infix notation into tokens"""
    expr = expr.replace(' ', '').replace('**', '^').replace('//', '$')

    tokens = []
    state = 'START'
    current_token = ''

    i = 0
    n = len(expr)

    while i < n:
        char = expr[i]

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
                if i + 1 < n:
                    next = expr[i + 1]
                else:
                    next = ''
                if next.isdigit():
                    state = 'NUMBER'
                    current_token = '-'
                    i += 1
                    continue
                elif next == '(':
                    tokens.append(Token('UNARY_MINUS', '~', 4))
                else:
                    raise TypeError(f'Неверный символ - {char}')
            else:
                raise TypeError(f'Неверный символ - {char}')

        elif state == 'NUMBER' or state == 'FLOAT':
            if char.isdigit():
                current_token += char
                i += 1
                continue
            elif char == '.':
                current_token += char
                i += 1
                continue
            else:
                tokens.append(Token('NUMBER', current_token, 0))
                current_token = ''
                state = 'START'
                continue

        i += 1

    if state == 'NUMBER':
        tokens.append(Token('NUMBER', current_token, 0))

    return tokens
