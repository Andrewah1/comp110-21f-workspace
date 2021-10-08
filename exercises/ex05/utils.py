"""List utility functions part 2."""

__author__ = "730389123"


def only_evens(x: list[int]) -> list[int]:
    """Pulls only even numbers from list."""
    y: list[int] = list()
    i: int = 0
    while i < len(x):
        if x[i] % 2 == 0:
            y.append(x[i])
        i += 1
    return y


def sub(x: list[int], y: int, z: int) -> list[int]:
    """Creates a sublist of a master list limited to specific integers."""
    a: list[int] = list()
    i: int = 0
    while i < len(x):
        if x[i] > y and x[i] <= z:
            a.append(x[i])
        i += 1
    return a


def concat(x: list[int], y: list[int]) -> list[int]:
    """Combines two lists."""
    z: list[int] = list()
    i: int = 0
    j: int = 0
    while i < len(x):
        z.append(x[i])
        i += 1 
    while j < len(y):
        z.append(y[j])
        j += 1
    return z