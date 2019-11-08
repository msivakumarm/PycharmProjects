import pytest

@pytest.mark.abc
def test_addition():
    print("a+b")

def test_multiplication():
    print("a*b")


def test_sub():
    print("a-b")