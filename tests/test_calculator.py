from src.models.token import Token
from src.power import *


def test_calculate_simple_addition():
    tokens = [
        Token("NUMBER", "2", 0),
        Token("NUMBER", "3", 0),
        Token("PLUS", "+", 1),
    ]
    result = calculate(tokens)
    assert result == 5.0


def test_calculate_subtraction():
    tokens = [
        Token("NUMBER", "10", 0),
        Token("NUMBER", "4", 0),
        Token("MINUS", "-", 1),
    ]
    result = calculate(tokens)
    assert result == 6.0


def test_calculate_multiplication():
    tokens = [
        Token("NUMBER", "7", 0),
        Token("NUMBER", "6", 0),
        Token("MUL", "*", 2),
    ]
    result = calculate(tokens)
    assert result == 42.0


def test_calculate_division():
    tokens = [
        Token("NUMBER", "20", 0),
        Token("NUMBER", "5", 0),
        Token("DIV", "/", 2),
    ]
    result = calculate(tokens)
    assert result == 4.0


def test_calculate_expression_with_multiple_ops():
    tokens = [
        Token("NUMBER", "2", 0),
        Token("NUMBER", "3", 0),
        Token("PLUS", "+", 1),
        Token("NUMBER", "4", 0),
        Token("MUL", "*", 2),
    ]
    result = calculate(tokens)
    assert result == 20.0
