"""An exercise in remainders and boolean logic."""

__author__ = "730389123"


number = int(input("enter an int: "))
if number % 2 == 0 and number % 7 == 0:
    print("TAR HEELS")
else:
    if number % 7 == 0:
        print("HEELS")
    if number % 2 == 0:
        print("TAR")
    if number % 2 != 0 and number % 7 != 0:
        print("CAROLINA")