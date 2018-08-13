numbers = input()

numbers_split = numbers.split()

first = int(numbers_split[0]) % 2
second = int(numbers_split[1]) % 2

if first + second == 1:
    print("YES")
else:
    print("NO")