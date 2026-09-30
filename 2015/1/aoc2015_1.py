# file = open('input_2015_1.txt', 'r')
# file = open(r'input_2015_1.txt', 'rt')

# INSTRUCTIONS = file.read()
# file.close()
# with open(r"input_2015_1.txt", 'rt') as file:
# with open(r"C:\Users\tt026085\Documents\AdventofCode\2015\1\input_2015_1.txt", 'rt') as file:
#     INSTRUCTIONS = file.read() 


# floor = position = 0
# basement_is_visited = False
# for index, character in enumerate(INSTRUCTIONS):
#     if character == '(':
#         floor += 1
#     else:
#         floor -= 1
#     if floor == -1 and not basement_is_visited:
#         position = index + 1
#         basement_is_visited = True

# print('Part 1:', floor)
# print('Part 2:', position)

with open(r"C:\Users\tt026085\Documents\AdventofCode\2015\1\input_2015_1.txt", 'rt') as file:
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
