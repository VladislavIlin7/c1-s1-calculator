import pytest

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


def test_calculate_floordiv():
    tokens = [
        Token("NUMBER", "22", 0),
        Token("NUMBER", "5", 0),
        Token("FLOORDIV", "//", 2),
    ]
    result = calculate(tokens)
    assert result == 4


def test_calculate_pow():
    tokens = [
        Token("NUMBER", "2", 0),
        Token("NUMBER", "5", 0),
        Token("POW", "**", 3),
    ]
    result = calculate(tokens)
    assert result == 32


def test_calculate_mod():
    tokens = [
        Token("NUMBER", "22", 0),
        Token("NUMBER", "5", 0),
        Token("MOD", "%", 2),
    ]
    result = calculate(tokens)
    assert result == 2


def test_calculate_invalid_arguments():
    tokens = [
        Token("NUMBER", "22", 0),
        Token("MOD", "%", 2)
    ]
    with pytest.raises(SyntaxError):
        calculate(tokens)


def test_calculate_too_many_arguments():
    tokens = [
        Token("NUMBER", "22", 0),
        Token("NUMBER", "23", 0)
    ]
    with pytest.raises(SyntaxError):
        calculate(tokens)


def test_calculate_mod_error():
    tokens = [
        Token("NUMBER", "22", 0),
        Token("NUMBER", "2.3", 0),
        Token("MOD", "%", 2)
    ]
    with pytest.raises(SyntaxError):
        calculate(tokens)


def test_calculate_floordiv_error():
    tokens = [
        Token("NUMBER", "22", 0),
        Token("NUMBER", "2.3", 0),
        Token("FLOORDIV", "//", 2)
    ]
    with pytest.raises(SyntaxError):
        calculate(tokens)
