from pathlib import Path

BASE_FOLDER = Path(__file__).parent

with open(BASE_FOLDER / 'input_2017_4.txt', 'r') as file:
    passphrase_list = file.read().splitlines()

def check_valid(passphrase: str) -> bool:
    word_list = passphrase.split()
    word_set = set(word_list)
    return len(word_list) == len(word_set)

valid = sum(check_valid(passphrase) for passphrase in passphrase_list)
print(valid)

# Part 2
def check_valid2(passphrase: str) -> bool:
    word_list = [''.join(sorted(word)) for word in passphrase.split()]
    word_set = set(word_list)
    return len(word_list) == len(word_set)

valid = sum(check_valid2(passphrase) for passphrase in passphrase_list)
print(valid)