"""Utility functions."""
from csv import DictReader


__author__ = "730389123"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]],) -> dict[str, list[str]]:
    """Produce a list[str] of all values in a single column."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a narrowed down dictionary."""
    result: dict[str, list[str]] = {}
    for column in table:
        if n >= len(table[column]):
            n = len(table[column])
        row_values: list[str] = []
        i: int = 0
        while i < n:
            row_values.append(table[column][i])
            i += 1
        result[column] = row_values
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a dictionary narrowe down by column."""
    result: dict[str, list[str]] = {}
    i: int = 0
    while i < len(columns):
        result[columns[i]] = []
        i += 1
    for column in result:
        result[column] = table[column]
    return result


def concat(table: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two tables."""
    result: dict[str, list[str]] = {}
    for column in table:
        result[column] = table[column]
    for column in table_2:
        if column in result:
            i: int = 0
            while i < len(table_2[column]):
                result[column].append(table_2[column][i])
                i += 1
        else:
            result[column] = table_2[column]
    return result


def count(strings: list[str]) -> dict[str, int]:
    """Produces a dictionary counting the number times a string appears."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(strings):
        if strings[i] in result:
            result[strings[i]] += 1
        else: 
            result[strings[i]] = 1
        i += 1
    return result