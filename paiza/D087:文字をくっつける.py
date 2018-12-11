row = int(input())
action = [input() for i in range(row)]

res = ""

for i in range(row):
	res = res + action[i]
	
print(res)