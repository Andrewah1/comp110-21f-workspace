"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730389123"


def test_invert_empty() -> None:
    """Edge Case Test."""
    xs: dict[str, str] = dict()
    assert invert(xs) == {}


def test_invert_one() -> None:
    """Test One."""
    xs: dict[str, str] = {'1': '2', '5': '6'}
    assert invert(xs) == {'2': '1', '6': '5'}


def test_invert_two() -> None:
    """Test Two."""
    xs: dict[str, str] = {'john': 'Steeve', 'Table': 'Chair', 'up': 'down', 'left': 'right'}
    assert invert(xs) == {'Steeve': 'john', 'Chair': 'Table', 'down': 'up', 'right': 'left'}


def test_favorite_color_empty() -> None:
    """Edge Case."""
    xs: dict[str, str] = dict()
    assert favorite_color(xs) == ""


def test_favorite_color_one() -> None:
    """Test one."""
    xs: dict[str, str] = {'john': 'red', 'jack': ' blue', 'Macy': 'red'}
    assert favorite_color(xs) == "red"


def test_favorite_color_two() -> None:
    """Test two."""
    xs: dict[str, str] = {'john': 'red', 'jack': ' blue', 'Macy': 'red', 'Brandon': 'green', 'steve': 'green'}
    assert favorite_color(xs) == "red"


def test_count_empty() -> None:
    """Edge case."""
    xs: list[str] = list()
    assert count(xs) == {}


def test_count_one() -> None:
    """Test one."""
    xs: list[str] = ["chair", "chair", "sky", "table", "ground"]
    assert count(xs) == {'chair': 2, 'sky': 1, 'table': 1, 'ground': 1}


def test_count_two() -> None:
    """Test two."""
    xs: list[str] = ["left", "left", "left", "left", "left", "left", "right"]
    assert count(xs) == {'left': 5, 'right': 1}