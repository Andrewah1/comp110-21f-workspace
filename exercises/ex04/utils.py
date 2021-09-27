"""List utility functions."""

__author__ = "730389123"


def all(x: list[int], y: int) -> bool:
    i: int = 0
    while i < len(x):
        z: int = x[i]
        if z != y:
            return False
        i += 1
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    if x == y:
        return True
    else:
        return False


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    while i < len(input):
        x: int = input[i]
        y: int = input[i + 1]
        if x >= y:
            return x
        i += 1