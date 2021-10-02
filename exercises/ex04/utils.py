"""List utility functions."""

__author__ = "730389123"


def all(x: list[int], y: int) -> bool:
    """Given a list return a bool indicating whether all the ints in the list are the same as the given int."""
    if len(x) == 0:
        return False
    i: int = 0
    while i < len(x):
        z: int = x[i]
        if z != y:
            return False
        i += 1
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    if x == y:
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """The max function is given a list of ints, max should return the largest in the List."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    if len(input) == 1:
        return input[0]
    i: int = 0
    highest: int = input[0]
    while i < len(input):
        x: int = input[i]
        if x > highest:
            highest = x
        i += 1
    return highest