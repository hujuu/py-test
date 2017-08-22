setting = input()
setting = setting.split()

n = int(setting[0])
days = int(setting[1])

rain_lst = []

for x in range(0, n):
	rains = input()
	rain_lst.append(rains)
	
rains_percent = []
days_lst = []

for x in range(0, n):
	rainy = rain_lst[x].split()
	rains_percent.append(int(rainy[1]))
	days_lst.append(int(rainy[0]))
	
ave_lst = []	

for x in range(0, n - days + 1):
	temp_lst = []
	for y in range(0, days):
		temp_lst.append(rains_percent[x + y])
	#print(temp_lst)
	ave = sum(temp_lst)/len(temp_lst)
	#print(ave)
	ave_lst.append(ave)
#print(ave_lst)
kouho = ([i for i, x in enumerate(ave_lst) if x == min(ave_lst)])
#print(kouho)
best_day = min(kouho)
#print(best_day)	
		
print(days_lst[best_day], days_lst[best_day] + days - 1)

