import math

number = input()
number = number.split()

print(math.floor((int(number[0]) / 100 + 1) * int(number[1])))
