from pathlib import Path
file_path = Path(__file__).parent / 'input_2015_3.txt'
file = open(file_path)
instructions = file.read()
location = 0+0j
movement = {'^': 1j, 'v': -1j, '>': 1, '<': -1}
houses = {location}
for direction in instructions:
    location += movement[direction]
    houses.add(location)

print(len(houses))

# PART 2
location_robo = location_santa = 0+0j
movement = {'^': 1j, 'v': -1j, '>': 1, '<': -1}
houses = {location_santa}
for index, direction in enumerate(instructions):
    if index % 2 == 0:
        location_santa += movement[direction]
        houses.add(location_santa)
    else:
        location_robo += movement[direction]
        houses.add(location_robo)

print(len(houses))


# Use class OOP
# class Santa:
#     def __init__(self) -> None:
#         self.location = 0 + 0j
#         self.movement = {'^': 1j, 'v': -1j, '>': 1, '<': -1}
#         self.houses = {self.location}

#     def move(self, direction: str) -> None:
#         self.location += self.movement[direction]
#         self.houses.add(self.location)

# # Part 1        
# santa = Santa()
# for direction in instructions:
#     santa.move(direction)

# print(len(santa.houses))

# # Part 2
# santa = Santa()
# robo_santa = Santa()
# for index in range(0, len(instructions), 2):
#     santa.move(instructions[index])
#     robo_santa.move(instructions[index+1])

# print(len(santa.houses | robo_santa.houses))


