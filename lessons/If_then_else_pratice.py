"""Pratice with If-Then-Else Statements."""

__author__ = "730389123"

choice: int = int(input("Enter a number: "))

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice > 75:
            print("D")
        else:
            print("C")
