size = input()
der = input()

size_split = size.split()
dr_split = der.split()

height = abs(int(size_split[0]) * int(dr_split[1]))
width = abs(int(size_split[1]) * int(dr_split[0]))
zone = abs(int(dr_split[0]) * int(dr_split[1]))

res = height + width - zone

print(res)
