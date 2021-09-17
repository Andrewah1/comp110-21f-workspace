"""Finding duplicate letters in a word."""

__author__ = "730389123"

word = str(input("Enter a word: "))
dup: bool = False 

i: int = 0
while i < len(word):
    char = str(word[i])
    j: int = i + 1
    while j < len(word):
        test = str(word[j])
        if char == test:
            dup: bool = True
        j = j + 1
    i = i + 1

if dup == False:
    print("Found duplicate: False")
else:
    print("Duplicate found: True")