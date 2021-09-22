"""Drawing forests in a loop."""

__author__ = "730389123"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
Depth = int(input("Depth: "))
forrest = TREE
if Depth > 0:
    print(forrest)
    Depth = Depth - 1
    i: int = 0
    while i < Depth:
        forrest = forrest + TREE
        i = i + 1
        print(forrest)