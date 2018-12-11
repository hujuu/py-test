number = input()

length = len(number)

point = 0

for count in range(length):
	if length > count + 1:
		if number[count] == number[count + 1]:
			point += 1

if point == length - 1:
	print(number)
else:
	print('No')