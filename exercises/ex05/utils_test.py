"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730389123"


def test_only_evens_empty() -> None:
    """Edge case test."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_one() -> None:
    """Generel test one."""
    xs: list[int] = [5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [6, 8, 10]


def test_only_evens_two() -> None:
    """General test two."""
    xs: list[int] = [25, 70, 110, 1000, 2577]
    assert only_evens(xs) == [70, 110, 1000]


def test_sub_empty() -> None:
    """Edge case test."""
    xs: list[int] = []
    j: int = 50
    k: int = 10000
    assert sub(xs, j, k) == []


def test_sub_one() -> None:
    """Generel test one."""
    xs: list[int] = [10, 60, 5000, 10000, 25, 100]
    j: int = 50
    k: int = 10000
    assert sub(xs, j, k) == [60, 5000, 10000, 100]


def test_sub_two() -> None:
    """General test two."""
    xs: list[int] = [-1, 15, 76, 99]
    j: int = -10
    k: int = 100
    assert sub(xs, j, k) == [-1, 15, 76, 99]


def test_concat_empty() -> None:
    """Edge case test."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_one() -> None:
    """Generel test one."""
    xs: list[int] = [15, 16, 17, 18]
    ys: list[int] = [20, 30, 50]
    assert concat(xs, ys) == [15, 16, 17, 18, 20, 30, 50]


def test_concat_two() -> None:
    """General test two."""
    xs: list[int] = [-10, 50, 100]
    ys: list[int] = [-100, 75, 10000]
    assert concat(xs, ys) == [-10, 50, 100, -100, 75, 10000]