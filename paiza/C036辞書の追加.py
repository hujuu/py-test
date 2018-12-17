first = input()
first = first.split()

two = input()
two = two.split()

first_rap = input()
second_rap = input()

first_dic = {}
second_dic = {}

for x in range(1, 5):
	temp = first_rap.split()
	first_dic[x] = int(temp[x-1])

win_lst = []

one_left = int(first[0])

if first_dic[one_left] < first_dic[int(first[1])]:
	win_lst.append(int(first[0]))
else:
	win_lst.append(int(first[1]))
	
if first_dic[int(two[0])] < first_dic[int(two[1])]:
	win_lst.append(int(two[0]))
else:
	win_lst.append(int(two[1]))

record_lst = []

for x in range(1, 3):
	temp = second_rap.split()
	record_lst.append(int(temp[x-1]))

if first_dic[int(two[0])] < first_dic[int(two[1])]:
	win_lst.append(int(two[0]))
else:
	win_lst.append(int(two[1]))

#print(record_lst)

if win_lst[0] < win_lst[1]:
	if record_lst[0] < record_lst[1]:
		print(win_lst[0])
		print(win_lst[1])
	else:
		print(win_lst[1])
		print(win_lst[0])
else:
	if record_lst[0] < record_lst[1]:
		print(win_lst[1])
		print(win_lst[0])
	else:
		print(win_lst[0])
		print(win_lst[1])
