import pytest

from hexlet_pytest.math_utils import clamp, is_even


def test_is_even_true_for_even_number():
    assert is_even(10) is True


def test_is_even_false_for_odd_number():
    assert is_even(7) is False


def test_clamp_inside_range():
    assert clamp(5, 1, 10) == 5


def test_clamp_below_range():
    assert clamp(-2, 0, 3) == 0


def test_clamp_above_range():
    assert clamp(10, 0, 3) == 3


def test_clamp_invalid_range():
    with pytest.raises(ValueError):
        clamp(1, 5, 2)
