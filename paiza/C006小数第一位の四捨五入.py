setting = input()
setting = setting.split()

scores = int(setting[0])
people = int(setting[1])
top = int(setting[2])

point = input()
point = point.split()

item_lst = []

for x in range(0, people):
	temp = input()
	temp = temp.split()
	item_lst.append(temp)
	
result_lst = []

for x in range(0, people):
	temp_list = []
	for y in range(0, scores):
		temp_list.append(float(point[y])*int(item_lst[x][y]))
	result_lst.append(round(sum(temp_list)))
	
#print(result_lst) 
result_lst.sort()

for x in range(1, top+1):
	print(result_lst[-x])