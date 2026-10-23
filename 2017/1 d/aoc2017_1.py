from pathlib import Path
file_path = Path(__file__).parent/ 'input_2017_1.txt'

with open(file_path) as file:
  data = file.read().strip()

sum1 = sum(int(data[i]) for i in range(-1, len(data) - 1) if data[i] == data[i + 1])
print(f'Part 1: {sum1}')

limit = int(len(data)/ 2)
sum2 = sum(int(data[i]) + int(data[i+ limit]) for i in range(limit - 1) if data[i] == data[i+ limit])
print(f'Part 2: {sum2}')