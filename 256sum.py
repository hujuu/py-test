n = int(input())

Ak = input()

Ak_split = Ak.split()

lst = []

for cnt in range(0, n):
	for m in range(cnt+1, n):
		res = int(Ak_split[cnt]) + int(Ak_split[m])
		
		lst.append(res)
		
if 256 in lst:
	print("yes")
else:
	print('no')