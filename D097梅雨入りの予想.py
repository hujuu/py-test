input_lines = input()

days = input_lines.split()

result = 0

for count in range(len(days)):
	result += int(days[count])

if result >= 5:
	print("yes")
else:
	print("no")
