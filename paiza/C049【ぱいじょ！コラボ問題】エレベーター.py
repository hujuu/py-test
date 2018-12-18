row = int(input())
action = [input() for i in range(row)]

result = 0

for count in range(row):
	if count == 0:
		move = int(action[count]) - 1
		result += abs(move)
	else:
		move = int(action[count]) - int(action[count - 1])
		result += abs(move)

print(result)
