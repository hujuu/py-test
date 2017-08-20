m = int(input())

n = int((m * m - m)/2)

lst = []
table = []

for x in range(0, n):
	ls = input()
	lst.append(ls)

for x in range(0, m):
	temp_lst = []
	
	for y in range(0, m-1):
		temp_lst.append("L")
		
	temp_lst.insert(x, "-")
	
	table.append(temp_lst)

for x in range(0, n):
	res = lst[x].split()
	row = int(res[0])
	col = int(res[1])
	#print(table[row-1][col-1])
	table[row-1][col-1] = "W"
	#print(table[row-1][col-1])
	
#print(table)

for x in range(0, m):
	print(' '.join(table[x]))
