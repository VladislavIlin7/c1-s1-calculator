from src.power import *
from src.models.token import Token


def test_convert_infix_to_rpn_simple_addition():
    tokens = [
        Token("NUMBER", "2", 0),
        Token("PLUS", "+", 1),
        Token("NUMBER", "3", 0),
    ]
    rpn = convert_infix_to_rpn(tokens)
    assert [t.value for t in rpn] == ["2", "3", "+"]


def test_convert_infix_to_rpn_operator_precedence():
    tokens = [
        Token("NUMBER", "2", 0),
        Token("PLUS", "+", 1),
        Token("NUMBER", "3", 0),
        Token("MUL", "*", 2),
        Token("NUMBER", "4", 0),
    ]
    rpn = convert_infix_to_rpn(tokens)
    assert [t.value for t in rpn] == ["2", "3", "4", "*", "+"]


def test_convert_infix_to_rpn_with_parentheses():
    tokens = [
        Token("LEFT", "(", 3),
        Token("NUMBER", "2", 0),
        Token("PLUS", "+", 1),
        Token("NUMBER", "3", 0),
        Token("RIGHT", ")", 3),
        Token("MUL", "*", 2),
        Token("NUMBER", "4", 0),
    ]
    rpn = convert_infix_to_rpn(tokens)
    assert [t.value for t in rpn] == ["2", "3", "+", "4", "*"]


def test_convert_infix_to_rpn_unary_minus():
    tokens = [
        Token("NUMBER", "-10", 0),
        Token("MINUS", "-", 1),
        Token("NUMBER", "15", 0),
    ]
    rpn = convert_infix_to_rpn(tokens)
    assert [t.value for t in rpn] == ["-10", "15", "-"]


def test_convert_infix_to_rpn_pow():
    tokens = [
        Token("NUMBER", "-10", 0),
        Token("POW", "**", 3),
        Token("NUMBER", "15", 0),
    ]
    rpn = convert_infix_to_rpn(tokens)
    assert [t.value for t in rpn] == ["-10", "15", "**"]


def test_convert_infix_to_rpn_floordiv():
    tokens = [
        Token("NUMBER", "-10", 0),
        Token("FLOORDIV", "//", 3),
        Token("NUMBER", "15", 0),
    ]
    rpn = convert_infix_to_rpn(tokens)
    assert [t.value for t in rpn] == ["-10", "15", "//"]


def test_convert_infix_to_rpn_mod():
    tokens = [
        Token("NUMBER", "-10", 0),
        Token("MOD", "%", 3),
        Token("NUMBER", "15", 0),
    ]
    rpn = convert_infix_to_rpn(tokens)
    assert [t.value for t in rpn] == ["-10", "15", "%"]
