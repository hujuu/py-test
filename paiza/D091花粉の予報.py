data = input().split()

res = 0

for cnt in range(len(data)):
	if int(data[cnt]) < 3:
		res += 1
		
print(res)