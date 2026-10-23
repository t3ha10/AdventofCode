from pathlib import Path
file_path = Path(__file__).parent / 'input_2015_2.txt'

with open(file_path) as file:
    data = [tuple(map(int, line.rstrip().split('x'))) for line in file.readlines()]

data_value = [(2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l), min(2*l+2*w, 2*w+2*h, 2*l+2*h) + (l*w*h)) for l, w, h in data]

total_paper = sum(item[0] for item in data_value)
total_ribbon = sum(item[1] for item in data_value)
print('Part 1:', total_paper)
print('Part 2:', total_ribbon)