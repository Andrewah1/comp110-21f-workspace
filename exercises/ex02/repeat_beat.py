"""Repeating a beat in a loop."""

__author__ = "730389123"


beat = str(input("What beat do you want to repeat? "))
string = beat
Counter: int = 0 
Maximum: int = int(input("How many times do you want to repeat it? "))
if Maximum > 0:
    Maximum = Maximum - 1 
    while Counter < Maximum: 
        string = string + " " + beat
        Counter = Counter + 1
    print(string)
else:
    print("No beat...")