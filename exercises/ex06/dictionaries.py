"""Practice with dictionaries."""

__author__ = "730389123"


def main() -> None:
    print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def invert(original: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    invert: dict[str, str] = dict()
    x: str = " "
    for key in original:
        x = original[key]
        invert[x] = key
    return invert


def favorite_color(colors: dict[str, str]) -> str:
    """Returns most common color in a dictionary."""
    color: str = " "
    i: int = 0
    color_list: list[str] = list()
    for key in colors:
        color_list.append(colors[key])
    j: int = 0
    while j < len(color_list):
        k: int = 0
        ct: int = 0
        y: str = color_list[j]
        while k < len(color_list):
            if color_list[k] == ct:
                ct += 1
            k += 1
        if i < ct:
            color = y
            i = ct
        j += 1
    return color


def count(content: list[str]) -> dict[str, int]:
    """Returns dictionary given a list with list and number of times an item appears in the list."""
    count: dict[str, int] = dict()
    i: int = 0
    while i < len(content):
        if content[i] in count:
            count[content[i]] += 1
        else:
            count[content[i]] = 1
    return count


if __name__ == "__main__":
    main()