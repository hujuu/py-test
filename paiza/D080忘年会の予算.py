data = input().split()

free = int(data[0]) * 6000

limit = int(data[1]) * 4000

print(free + limit)


def menu_sum(a, b):
	res = a * 6000 + b * 4000
	return res


print(menu_sum(int(data[0]), int(data[1])))
