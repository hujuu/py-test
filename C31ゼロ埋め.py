from collections import OrderedDict

n = int(input())
nation_lst = []
nation_dic = OrderedDict()

for x in range(0, n):
    nation_time = input().split()
    nation_dic[nation_time[0]] = nation_time[1]

base = input().split()

basic_time = int(base[1][0:2]) - int(nation_dic[base[0]])
if basic_time < 0:
    basic_time = basic_time + 24

number_pad = '{0:02d}'.format(basic_time)

for x in nation_dic:
    hour = int(number_pad) + int(nation_dic[x])
    if hour > 23:
        hour = hour - 24
    print('{0:02d}'.format(hour) + base[1][2:5])
