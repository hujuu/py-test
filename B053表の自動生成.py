preset = input()
height = int(preset.split()[0])
width = int(preset.split()[1])
position = [input() for i in range(2)]

column1_case = int(position[1].split()[0]) - int(position[0].split()[0])
column1_1 = int(position[0].split()[0])
column1 = [column1_1 + i * column1_case for i in range(height)]

column2_case = int(position[1].split()[1]) - int(position[0].split()[1])
column2_1 = int(position[0].split()[1])
column2 = [column2_1 + i * column2_case for i in range(height)]

row_all = []

for rows in range(height):
    row1_case = column2[rows] - column1[rows]
    row1_1 = column1[rows]
    row1 = [row1_1 + i * row1_case for i in range(width)]
    # print(row1)
    print(' '.join(map(str, row1)))

