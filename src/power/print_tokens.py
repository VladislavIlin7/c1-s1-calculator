from src.models.token import Token
from array import array



def print_tokens(tokens: array[Token]):
    for i in tokens:
        print(i.type, i.value)
