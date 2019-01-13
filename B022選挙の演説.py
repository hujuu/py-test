preset = input()
time_len = int(preset.split()[2])
position = [input() for i in range(time_len)]

elect = {str(x): 0 for x in range(1, int(preset.split()[0]) + 1)}

elect['neutral'] = int(preset.split()[1])

# print(elect)

for speech in position:
    for key, value in elect.items():
        if value > 0:
            elect[key] = elect[key] - 1
            elect[speech] = elect[speech] + 1

# print(elect)

del elect['neutral']

max_val = max(elect.values())
keys_of_max_val = [key for key in elect if elect[key] == max_val]

# print(keys_of_max_val)

for result in keys_of_max_val:
    print(result)
