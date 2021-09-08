"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730389123"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


number = randint(1, 4)
print("Your fortune cookie says. . .")
if number == 1:
    print("It will be Wednesday my dudes.")
else:
    if number == 2:
        print("Let's say hypothetically for the sake of argument something special will happen.")
    else:
        if number == 3:
            print("your life will go xgames mode.")
        else:
            print("you will a receive a bqq and foot massage in the near future.")
print("Now, go spread positive vibes!")
