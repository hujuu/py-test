basic_info = input()
basic_info = basic_info.split()
set_list = [input() for i in range(int(basic_info[0]))]

for i, judge in enumerate(set_list):
    judge = judge.split()
    res = int(judge[0]) - int(judge[1]) * 5
    if res >= int(basic_info[1]):
        print(i + 1)
    elif res < 0 | int(basic_info[1]) == 0:
        print(i + 1)
