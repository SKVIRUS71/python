import pytest
from main import add, sub, mul, div

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5

def test_mul():
    assert mul(4, 2.5) == 10
    assert mul(0, 123) == 0

def test_div():
    assert div(6, 2) == 3
    assert abs(div(1, 3) - 0.33333333) < 1e-7

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(1, 0)

