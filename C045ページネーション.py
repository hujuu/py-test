import math

row = input()

sp = row.split()

total = int(sp[0])
limit = int(sp[1])
order = int(sp[2])

pages = math.ceil(total/limit)

if pages < order:
	print("none")
else:
	start = limit * (order - 1)
	for page in range(limit):
		start += 1
		if page == limit - 1:
			print(start)
		else:
			print(start, end=" ")
