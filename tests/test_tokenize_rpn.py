import pytest
from src.power import *


def test_tokenize_rpn_simple():
    tokens = tokenize_rpn("3 2 +")
    assert [t.type_token for t in tokens] == ["NUMBER", "NUMBER", "PLUS"]
    assert [t.value for t in tokens] == ["3", "2", "+"]


def test_tokenize_rpn_pow():
    tokens = tokenize_rpn("3 2 **")
    assert [t.type_token for t in tokens] == ["NUMBER", "NUMBER", "POW"]
    assert [t.value for t in tokens] == ["3", "2", "**"]


def test_tokenize_rpn_floordiv():
    tokens = tokenize_rpn("3 2 //")
    assert [t.type_token for t in tokens] == ["NUMBER", "NUMBER", "FLOORDIV"]
    assert [t.value for t in tokens] == ["3", "2", "//"]


def test_tokenize_rpn_mod():
    tokens = tokenize_rpn("3 2 %")
    assert [t.type_token for t in tokens] == ["NUMBER", "NUMBER", "MOD"]
    assert [t.value for t in tokens] == ["3", "2", "%"]


def test_tokenize_rpn_complex():
    tokens = tokenize_rpn("~321 4 - 2 *")
    assert [t.type_token for t in tokens] == ["NUMBER", "NUMBER", "MINUS", "NUMBER", "MUL"]
    assert [t.value for t in tokens] == ["-321", "4", "-", "2", "*"]


def test_tokenize_exception():
    with pytest.raises(ValueError):
        tokenize_infix("9 5f + +")
