preset = input()
time_len = int(preset.split()[0])
position = [input() for i in range(time_len)]

x = int(preset.split()[1])
y = int(preset.split()[2])

x_list = [x]

for count in position:
    x = x + int(count.split()[0])
    y = y + int(count.split()[1])

    if y <= 0:
        break
    else:
        x_list.append(x)

print(max(x_list))
