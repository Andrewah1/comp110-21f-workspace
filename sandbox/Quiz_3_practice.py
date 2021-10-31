"""Quiz 3 Pratice."""


def dict_transform(x: dict[int, list[int]]) -> dict[int, list[int]]:
    """Fuction which multiplies all values by the key."""
    for key in x:
        for i in range(len(x[key])):
            x[key][i] *= key
    return x


def average_grade(grades: dict[str, list[int]]) -> dict[str, float]:
    """Averages grade."""
    averages: dict[str, float] = {}
    for student in grades:
        total: int = 0
        for grade in grades[student]:
            total += grade
            averages[student] = total / len(grades[student])
    return averages