row = input()

sp = row.split()

# print(sp)

res = int(sp[0]) - int(sp[1])

if res < 0:
	res = res * -1
	
print(res)