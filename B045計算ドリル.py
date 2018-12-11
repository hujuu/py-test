import random

setting = input()
set_data = setting.split()

plus = int(set_data[0])
minus = int(set_data[1])

res = []

plus_count = 0

while plus_count < plus:
	left = random.randint(0, 99)
	right = random.randint(0, 99 - left)
	
	temp = [left, right]
	
	if temp not in res:
		res.append(temp)
		plus_count += 1

for gen in range(plus):
	print(res[gen][0], "+", res[gen][1], "=")

res = []
count = 0

while count < minus:
	left = random.randint(0, 99)
	right = random.randint(0, 99 - left)
	
	temp = [left, right]
	
	if temp not in res:
		res.append(temp)
		count += 1

for gen in range(minus):
	print(res[gen][0], "-", res[gen][1], "=")
