# coding: utf-8
import math

input_line = input()
init = input_line.split()

kcals = [input() for i in range(int(init[0]))]
eats = [input() for i in range(int(init[1]))]

for x in range(int(init[1])):
    cal = eats[x].split()
    sums = 0
    for n in range(int(init[0])):
        sums += int(cal[n]) * int(kcals[n]) / 100
        sums = math.floor(sums)
        
    print(sums)
