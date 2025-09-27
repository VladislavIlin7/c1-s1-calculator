from src.models.token import Token
from array import array

def tokenize_infix(expr: str) -> array[Token]:
    expr = expr.replace(' ', '')  # remove spaces
    tokens = []
    state = 'START'
    current_token = ''

    # 1+2 -> [1]
    for char in expr:
        if char == ' ':
            state = 'START'
        elif state == 'START':
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
            elif char == '(':
                tokens.append(Token('LEFT', char, 3))
            elif char == ')':
                tokens.append(Token('RIGHT', char, 3))
            elif char == '.':
                state = 'FLOAT'
            elif char == '~':
                current_token += '-'
                state = 'NUMBER'
            else:
                raise 'Неверный символ'

            # дописать, не забываем про числа с точкой

        elif state == 'NUMBER' or state == 'FLOAT':
            if char.isdigit():
                current_token += char
            elif char == '.':
                current_token += char
            else:
                tokens.append(Token('NUMBER', current_token, 0))
                if char == '+':
                    tokens.append(Token('PLUS', char, 1))
                    state = 'START'
                    current_token = ''
                elif char == '-':
                    tokens.append(Token('MINUS', char, 1))
                    state = 'START'
                    current_token = ''
                elif char == '*':
                    tokens.append(Token('MUL', char, 2))
                    state = 'START'
                    current_token = ''
                elif char == '/':
                    tokens.append(Token('DIV', char, 2))
                    state = 'START'
                    current_token = ''
                elif char == '(':
                    tokens.append(Token('LEFT', char, 3))
                    state = 'START'
                    current_token = ''
                elif char == ')':
                    tokens.append(Token('RIGHT', char, 3))
                    state = 'START'
                    current_token = ''

            # дописать
        # дописать

    # Завершающая обработка
    if state == 'NUMBER':
        tokens.append(Token('NUMBER', current_token, 0))

    return tokens



