import pytest
from src.power import *


def test_tokenize_simple():
    tokens = tokenize_infix("123*2")
    assert [t.type_token for t in tokens] == ["NUMBER", "MUL", "NUMBER"]
    assert [t.value for t in tokens] == ["123", "*", "2"]


def test_tokenize_with_spaces():
    tokens = tokenize_infix(" 3    * 4 ")
    assert [t.type_token for t in tokens] == ["NUMBER", "MUL", "NUMBER"]
    assert [t.value for t in tokens] == ["3", "*", "4"]


def test_tokenize_float():
    tokens = tokenize_infix("2.5+1.5")
    assert [t.type_token for t in tokens] == ["NUMBER", "PLUS", "NUMBER"]
    assert [t.value for t in tokens] == ["2.5", "+", "1.5"]


def test_tokenize_unary_minus():
    tokens = tokenize_infix("~10 -15")
    assert [t.type_token for t in tokens] == ["NUMBER", "MINUS", "NUMBER"]
    assert [t.value for t in tokens] == ["-10", '-', '15']


def test_tokenize_pow():
    tokens = tokenize_infix("2**4")
    assert [t.type_token for t in tokens] == ["NUMBER", "POW", "NUMBER"]
    assert [t.value for t in tokens] == ["2", "^", "4"]


def test_tokenize_floordiv():
    tokens = tokenize_infix("9//4")
    assert [t.type_token for t in tokens] == ["NUMBER", "FLOORDIV", "NUMBER"]
    assert [t.value for t in tokens] == ["9", "$", "4"]


def test_tokenize_mod():
    tokens = tokenize_infix("9%4")
    assert [t.type_token for t in tokens] == ["NUMBER", "MOD", "NUMBER"]
    assert [t.value for t in tokens] == ["9", "%", "4"]


def test_tokenize_exception():
    with pytest.raises(TypeError):
        tokenize_infix("9%4r")
