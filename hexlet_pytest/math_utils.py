"""Utility math helpers for demo."""


def is_even(number):
    return number % 2 == 0


def clamp(number, min_value, max_value):
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")
    return max(min_value, min(number, max_value))
