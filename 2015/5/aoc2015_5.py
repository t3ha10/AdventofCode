from pathlib import Path

file_path = Path(__file__).parent/ 'input_2015_5.txt'
def is_enough_vowels(word):
    # return len([character for character in word if character in 'aeiou']) >= 3
    return sum(letter in 'aeiou' for letter in word) >= 3
def is_contain_twice(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False

def is_not_contain(word):
    sequence = ['ab', 'cd', 'pq', 'xy']
    for case in sequence:
        if word.find(case) != -1:
            return False
    return True

def is_contain_pair(word):
    for i in range(len(word) - 1):
        for j in range(i + 2, len(word) - 1):
            if j != i and j + 1 != i + 1:
                if word[i] + word[i + 1] == word[j] + word[j + 1]:
                    return True
    return False
def is_contain_repeat_letter(word):
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            return True
    return False




with open(file_path) as file:
    total1 = 0
    total2 = 0
    for line in file:
        if is_enough_vowels(line) and is_contain_twice(line) and is_not_contain(line):
            total1 += 1
        if is_contain_pair(line) and is_contain_repeat_letter(line):
            total2 += 1
    print('Part 1: ', total1)
    print('Part 2: ', total2)
