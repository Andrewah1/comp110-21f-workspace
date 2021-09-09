"""Counting letters in a string."""

__author__ = "730389123"


letter = str(input("What letter do you want to seach for?: "))
word = str(input("Enter a word: "))
i: int = 0
maximun: int = len(word)
letter_count: int = 0
while i < maximun:
    if word[i] == letter:
        letter_count = letter_count + 1
    i = i + 1
print("Count:", letter_count)