import math

row = input()

sp = row.split()

# print(sp)

price = int(sp[0])
discount = int(sp[1])

after_price = price
total = price
count = 0

while after_price > 0:
	# 切り捨て
	after_price = math.floor(after_price * (100 - discount)/100)
	total += after_price
	
print(total)
