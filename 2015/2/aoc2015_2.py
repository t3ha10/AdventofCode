file = open(r'C:\Users\tt026085\Documents\AdventofCode\2015\2\input_2015_2.txt', 'rt')
DIMENSIONS = file.read()

sum_paper = 0
sum_ribbon = 0
for line in DIMENSIONS.split():
    present = line.split('x')
    l = int(present[0])
    w = int(present[1])
    h = int(present[2])
    present_area = 2*l*w + 2*w*h + 2*h*l
    sum_paper += present_area
    present_extra = min(l*w, w*h, h*l)
    sum_paper += present_extra
    smallest_perimeter = 2 * (min(l+w, w+h, h+l))
    sum_ribbon += smallest_perimeter
    bow = l * w * h
    sum_ribbon += bow
 
print(f"{sum_paper = }")
print(f"{sum_ribbon = }")
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