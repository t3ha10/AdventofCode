from pathlib import Path
file_path = Path(__file__).parent / "input_2015_1.txt"
with open(file_path) as file:
    INSTRUCTIONS = file.read() 


floor = position = 0
basement_is_visited = False
for index, character in enumerate(INSTRUCTIONS):
    if character == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1 and not basement_is_visited:
        position = index + 1
        basement_is_visited = True

print('Part 1:', floor)
print('Part 2:', position)
