# file = open(r'C:\Users\tt026085\Documents\AdventofCode\2015\2\input_2015_2.txt', 'rt')
# DIMENSIONS = file.read()
# with open(r'C:\Users\tt026085\Documents\AdventofCode\2015\2\input_2015_2.txt', 'rt') as file:
#     DIMENSIONS = file.read()


# sum_paper = 0
# sum_ribbon = 0
# for line in DIMENSIONS.split():
#     present = line.split('x')
#     l = int(present[0])
#     w = int(present[1])
#     h = int(present[2])
#     present_area = 2*l*w + 2*w*h + 2*h*l
#     sum_paper += present_area
#     present_extra = min(l*w, w*h, h*l)
#     sum_paper += present_extra
#     smallest_perimeter = 2 * (min(l+w, w+h, h+l))
#     sum_ribbon += smallest_perimeter
#     bow = l * w * h
#     sum_ribbon += bow
 
# print(f"{sum_paper = }")
# print(f"{sum_ribbon = }")
# total_paper = 0

# Toinen tapa (lyhyempi mutta sekävämpi)
# for line in DIMENSIONS.strip().splitlines():
#     l, w, h = map(int, line.split('x'))
#     total_paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

# print(f'{total_paper = }')

# for line in DIMENSIONS.strip().splitlines():
#     present = line.split('x')

#     l = int(present[0])
#     w = int(present[1])
#     h = int(present[2])

#     present_area = 2*l*w + 2*w*h + 2*h*l
#     present_extra = min(l*w, w*h, h*l)

#     present_paper = 2*l*w + 2*w*h + 2*h*l + present_extra
#     total_paper += present_paper

# print(f'{total_paper = }')

# with open(r'C:\Users\tt026085\Documents\AdventofCode\2015\2\input_2015_2.txt', 'r') as file:
#     data = []
#     for line in file.readlines():
#         data.append(tuple(map(int, line.rstrip().split('x'))))
# paper = 0
# ribbon = 0
# for l, w, h in data:
#     paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
#     ribbon += min(2*l+2*w, 2*w+2*h, 2*l+2*h) + (l*w*h)
# print('Part 1:', paper)
# print('Part 2:', ribbon)


with open(r'C:\Users\tt026085\Documents\AdventofCode\2015\2\input_2015_2.txt', 'r') as file:
    data = [tuple(map(int, line.rstrip().split('x'))) for line in file.readlines()]

data_value = [(2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l), min(2*l+2*w, 2*w+2*h, 2*l+2*h) + (l*w*h)) for l, w, h in data]

total_paper = sum([data_value[i][0] for i in range(len(data_value))])
total_ribbon = sum([data_value[i][1] for i in range(len(data_value))])
print('Part 1:', total_paper)
print('Part 2:', total_ribbon)