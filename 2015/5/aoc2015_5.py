from pathlib import Path
from typing import Generator

file_path = Path(__file__).parent/ 'input_2015_5.txt'

def get_substrings(string: str, length: int = 2) -> Generator[str]:
    return (string[index:index+length] for index in range(len(string)-(length-1)))

def rule1(word):
    return sum(letter in 'aeiou' for letter in word) >= 3

def rule2(word):
    for pair in get_substrings(word):
        if pair[0] == pair[1]:
            return True
    return False

def rule3(word):
    for pair in get_substrings(word):
        if pair in ('ab', 'cd', 'pq', 'xy'):
            return False
    return True

def rule4(word):
    for index, pair in enumerate(get_substrings(word)):
        if pair in word[index+2:]:
            return True
    return False

def rule5(word):
    for substring in get_substrings(word, length=3):
        if substring[0] == substring[-1]:
            return True
    return False

def is_nice1(word: str) -> bool:
    return rule1(word) and rule2(word) and rule3(word)

def is_nice2(word: str) -> bool:
    return rule4(word) and rule5(word)

with open(file_path) as file:
    strings = file.read()
total = sum(is_nice1(line) for line in strings.splitlines())
print(f'Part 1: {total}')

total = sum(is_nice2(line) for line in strings.splitlines())

print(f'Part 2: {total}')