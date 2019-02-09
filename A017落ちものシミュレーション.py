# coding: utf-8
import numpy as np

preset = input()
height = int(preset.split()[0])
width = int(preset.split()[1])
time_len = int(preset.split()[2])
blocks = [input() for i in range(time_len)]

# field = np.zeros((height, width))
field = [[0] * width] * height
# print(field)

result = []

for cnt in blocks:
    block = cnt.split()
    block_data = [[1] * int(block[1])] * int(block[0])

    # block_data.insert(space, 0)
    # print(block_data)

    space1 = int(block[2])
    space2 = width - int(block[2])

    # print(space1, space2)
    # print(block_data[0])

    for i in range(space1):
        block_data[0].insert(0, 0)

    for j in range(width - len(block_data[0])):
        block_data[0].append(0)

    # print(block_data)
    result.append(block_data)

print(result)
# print(result[0])
field[6] = result[0][0]
field[5] = [1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
field[4] = [1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
field[3] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
field[2] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
field[1] = [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]


for mapping in field:
    # print(mapping)
    row = ''
    for pixel in mapping:
        if pixel == 0:
            row = row + '.'
        else:
            row = row + '#'
    print(row)

