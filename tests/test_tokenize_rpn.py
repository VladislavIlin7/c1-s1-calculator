from src.power import *


def test_tokenize_rpn_simple():
    tokens = tokenize_rpn("3 2 +")
    assert [t.type for t in tokens] == ["NUMBER", "NUMBER", "PLUS"]
    assert [t.value for t in tokens] == ["3", "2", "+"]

def test_tokenize_rpn_POW():
    tokens = tokenize_rpn("3 2 **")
    assert [t.type for t in tokens] == ["NUMBER", "NUMBER", "POW"]
    assert [t.value for t in tokens] == ["3", "2", "**"]

def test_tokenize_rpn_FLOORDIV():
    tokens = tokenize_rpn("3 2 //")
    assert [t.type for t in tokens] == ["NUMBER", "NUMBER", "FLOORDIV"]
    assert [t.value for t in tokens] == ["3", "2", "//"]

def test_tokenize_rpn_MOD():
    tokens = tokenize_rpn("3 2 %")
    assert [t.type for t in tokens] == ["NUMBER", "NUMBER", "MOD"]
    assert [t.value for t in tokens] == ["3", "2", "%"]

def test_tokenize_rpn_complex():
    tokens = tokenize_rpn("~321 4 - 2 *")
    assert [t.type for t in tokens] == ["NUMBER", "NUMBER", "MINUS", "NUMBER", "MUL"]
    assert [t.value for t in tokens] == ["-321", "4", "-", "2", "*"]