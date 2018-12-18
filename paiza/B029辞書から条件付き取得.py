xy = input().split()

x = int(xy[0])
y = int(xy[1])

k = int(input())

n = int(input())

point_lst = []

for count in range(0, n):
	point = input().split()
	point_lst.append(point)
		
len_lst = []
price_dic = {}

for count in range(0, n):
	xi = int(point_lst[count][0])
	yi = int(point_lst[count][1])
	price = int(point_lst[count][2])
	length = (x - xi)**2 + (y - yi)**2
	len_lst.append(length)
	
	price_dic[price] = length

len_lst.sort()

res = [key for key, v in price_dic.items() if v <= len_lst[k-1]]

import numpy as np

ave = np.average(res)      # 平均を計算
print(int(ave))   # 結果を表示
