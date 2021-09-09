"""Repeating a beat in a loop."""

__author__ = "730389123"


beat = str(input("What beat do you want to repeat? "))
Counter: int = 0 
Maximun: int = int(input("How many times do you want to repeat it? "))
while Counter < Maximun:
    Counter = Counter + 1
    print(beat, end=" ")
if Counter <= 0:
    print("No beat...") 