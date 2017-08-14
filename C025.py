capa = int(input())
n = int(input())

fax_lst = []

for x in range(0, n):
	fax = input()
	fax_lst.append(fax)
	
paper_count = []

count = 0	
hour = 0	
	
for x in range(0, n):
	faxs = fax_lst[x].split()
	
	if x == 0:
		count = count + int(faxs[2])
		hour = int(faxs[0])
	elif int(faxs[0]) == hour:
		count = count + int(faxs[2])
		if x == n-1:
			paper_count.append(count)
	else:
		paper_count.append(count)
		count = int(faxs[2])
		hour = int(faxs[0])
		if x == n:
			paper_count.append(count)

num_lst = []

for x in range(0, len(paper_count)):
	num = 0
	cou = 0
	if paper_count[x] > capa:
		while num < paper_count[x]:
			num = num + capa
			cou = cou + 1
	else:
		cou = 1
	num_lst.append(cou)

print(sum(num_lst))