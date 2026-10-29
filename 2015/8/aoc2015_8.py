from pathlib import Path
import re

file_path = Path(__file__).parent / 'input_2015_8.txt'

def count_characters(line):
  return len(line)

def count_special_characters(line):
  # hexadecimal_chars = re.findall(r'\\x[0-9a-f][0-9a-f]', line)
  # escape_chars = re.findall(r"\\(?!x).", line)
  # return len(hexadecimal_chars) * 3 + len(escape_chars) + 2
  escape_chars = re.findall(r"\\x[0-9a-f][0-9a-f]|\\.|.", line)
  return len(escape_chars) - 2

with open(file_path) as f:
  result = 0
  for line in f:
    line = line.strip()
    # result += count_special_characters(line)
    result += count_characters(line) - count_special_characters(line)
  print(result)

