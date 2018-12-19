n = int(input())

medal_lst = []

lst = []

for x in range(0, n):
	medal = input()
	medal_lst.append(medal)
	
for x in range(0, n):
	temp_list = []
	three_medals = medal_lst[x].split()
	
	for y in range(0, 3):
		count = int(three_medals[y])
		temp_list.append(count)
		
	lst.append(temp_list)

lst.sort(key=lambda x:(x[0],x[1],x[2]))

for x in range(0, n):
	print(lst[n-1-x][0], lst[n-1-x][1], lst[n-1-x][2])