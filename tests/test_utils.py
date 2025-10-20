import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import multiply, divide


def test_multiply_normal():
    assert multiply(2, 3, 4) == 24


def test_multiply_with_zero():
    assert multiply(5, 0, 10) == 0


def test_multiply_negative():
    assert multiply(-2, 3) == -6


def test_divide_normal():
    assert divide(100, 5, 2) == 10


def test_divide_by_zero():
    assert divide(10, 0) == "Error: Division by zero is not allowed"


def test_divide_no_args():
    assert divide() == "Error: No numbers provided"
