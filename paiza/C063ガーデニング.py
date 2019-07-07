
input_line = int(input())

seeds = [input() for i in range(input_line)]

dic = {}

blow_day = []

for count in range(input_line):
    info = seeds[count].split()
    blow = int(info[0]) + int(info[1])
    blow_day.append(blow)

for insert in range(max(blow_day)):
    dic[insert + 1] = 0

for count in range(input_line):
    info = seeds[count].split()
    blow = int(info[0]) + int(info[1])
    dic[blow] = dic[blow] + 1

# print(max(dic))

max_k_list = [kv[0] for kv in dic.items() if kv[1] == max(dic.values())]
# print(max_k_list)
print(min(max_k_list))
