data1 = input().split()
data2 = input().split()

res1 = int(data1[2]) / ( int(data1[0]) * int(data1[1]) )
res2 = int(data2[2]) / ( int(data2[0]) * int(data2[1]) )

if res1 > res2:
	print(data2[0], data2[1], data2[2])
elif res2 > res1:
	print(data1[0], data1[1], data1[2])
else:
	print('DRAW')