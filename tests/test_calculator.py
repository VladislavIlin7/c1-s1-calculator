import pytest
from src.power import tokenize_infix, tokens_to_RPN, calculator

# --- Tokenize tests ---
def test_tokenize_simple():
    tokens = tokenize_infix("1+2")
    assert [t.type for t in tokens] == ["NUMBER", "PLUS", "NUMBER"]
    assert [t.value for t in tokens] == ["1", "+", "2"]

def test_tokenize_with_spaces():
    tokens = tokenize_infix(" 3 * 4 ")
    assert [t.type for t in tokens] == ["NUMBER", "MUL", "NUMBER"]
    assert [t.value for t in tokens] == ["3", "*", "4"]

def test_tokenize_float():
    tokens = tokenize_infix("2.5+1.5")
    assert [t.type for t in tokens] == ["NUMBER", "PLUS", "NUMBER"]
    assert [t.value for t in tokens] == ["2.5", "+", "1.5"]

def test_tokenize_unary_minus():
    tokens = tokenize_infix("~10")
    assert [t.type for t in tokens] == ["NUMBER"]
    assert [t.value for t in tokens] == ["-10"]

# --- RPN conversion tests ---
def test_rpn_order():
    tokens = tokenize_infix("3+4*2")
    rpn = tokens_to_RPN(tokens)
    assert [t.value for t in rpn] == ["3", "4", "2", "*", "+"]

def test_rpn_parentheses():
    tokens = tokenize_infix("(3+4)*2")
    rpn = tokens_to_RPN(tokens)
    assert [t.value for t in rpn] == ["3", "4", "+", "2", "*"]

# --- Calculator tests ---
@pytest.mark.parametrize("expr,expected", [
    ("1+2", 3.0),
    ("2*3+4", 10.0),
    ("(2+3)*4", 20.0),
    ("10/2+7", 12.0),
    ("(10-8*(5+5))/10", -7.0),
    ("(~10-8*(5+5))/10", -9.0),
])
def test_calculator(expr, expected):
    tokens = tokenize_infix(expr)
    rpn = tokens_to_RPN(tokens)
    result = calculator(rpn)
    assert result == pytest.approx(expected)