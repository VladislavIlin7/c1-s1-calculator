import pytest
from src.power import *


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
    rpn = convert_infix_to_rpn(tokens)
    result = calculate(rpn)
    assert result == pytest.approx(expected)