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