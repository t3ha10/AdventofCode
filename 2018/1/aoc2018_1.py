from pathlib import Path

BASE_FOLDER = Path(__file__).parent

with open(BASE_FOLDER /'input_2018_1.txt', 'r') as file:
    data: list[int] = [int(line) for line in file]

## Part 1
print(sum(data))

## Part 2

freq_history = set() # {}
current_freq = index = 0
while current_freq not in freq_history:
    freq_history.add(current_freq)
    current_freq += data[index]
    index = (index + 1) % len(data)


print(current_freq)