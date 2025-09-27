from src.power import *


# --- RPN conversion tests ---
def test_rpn_order():
    tokens = tokenize_infix("3+4*2")
    rpn = convert_infix_to_rpn(tokens)
    assert [t.value for t in rpn] == ["3", "4", "2", "*", "+"]

def test_rpn_parentheses():
    tokens = tokenize_infix("(3+4)*2")
    rpn = convert_infix_to_rpn(tokens)
    assert [t.value for t in rpn] == ["3", "4", "+", "2", "*"]

