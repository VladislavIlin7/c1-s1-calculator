from src.models.token import Token
from array import array

def power_function(target: int, power: int ) -> float:
    """
    Пример функции, которая выполняет операцию возведения в степень
    :param target:  Число, которое будут возводить в степень
    :param input_two: Степень в которую будут возводить число
    :return: Возвращает число возведенное в степень
    """
    return pow(target, power)

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


def tokens_to_RPN(tokens: array[Token]) -> array[Token]:
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



def calculator(tokens: array[Token]) -> float:
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



def print_tokens(tokens: array[Token]):
    for i in tokens:
        print(i.type, i.value)
