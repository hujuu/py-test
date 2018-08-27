number = int(input())
important = input()
words = [input() for i in range(number)]

i = 0

for judge in words:
    if important in judge:
        print(judge)
        i = i + 1

if i == 0:
    print("None")
