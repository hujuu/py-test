count = int(input())

lst = []

top = int((count-1)/2)

y = "y"

res = ""

if count % 2 == 0:
	print("invalid")
elif count == 1:
	print(y)
else:
	for row in range(top):
		#lst = []
		res = ""
		for col in range(count):
			if col == row:
				#lst.append(y)
				res = res + y
			elif col == count - row -1:
				#lst.append(y)
				res = res + y
			else:
				lst.append(".")
				res = res + "."
		#print(lst)
		print(res)
	for row in range(top + 1):
		res = ""
		for col in range(count):
			if col == top:
				res = res + y
			else:
				res = res + "."
		print(res)
