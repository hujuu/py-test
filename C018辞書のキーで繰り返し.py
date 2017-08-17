import math
n = int(input())
recipe_lst = []

for x in range(0, n):
	recipe = input()
	recipe_lst.append(recipe)

recipe_dic = {}

for x in range(0, n):
	dict_in = recipe_lst[x].split()
	recipe_dic.update({dict_in[0]:int(dict_in[1])})

m = int(input())
stock_lst = []

for x in range(0, m):
	stock = input()
	stock_lst.append(stock)

stock_dic = {}

for x in range(0, m):
	dict_in = stock_lst[x].split()
	stock_dic.update({dict_in[0]:int(dict_in[1])})

count = []

for k in recipe_dic.keys():
	try:
		temp_count = stock_dic[k] / recipe_dic[k]
		count.append(math.floor(temp_count))
	except KeyError:
		count.append(0)
	
print(min(count))