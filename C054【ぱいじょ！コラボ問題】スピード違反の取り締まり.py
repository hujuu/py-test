import sys

segment_point = input()
key = segment_point.split()
catch = [input() for i in range(int(key[0]))]

for test in range(int(key[0]) - 1):
    a = catch[test].split()
    b = catch[test + 1].split()

    time = int(b[0]) - int(a[0])

    length = int(b[1]) - int(a[1])

    res = length / time

    if res > int(key[1]):
        print("YES")
        sys.exit()

print("NO")

