# coding: utf-8
import sys

nm = input().split()

n = int(nm[0])
m = int(nm[1])

if n == 0:
	print(0)
	sys.exit()
	
if m == 0:
	print(0)
	sys.exit()

live_lst = []

for x in range(0, m):
	live = input().split()
	live_lst.append(live)

res = 0

for x in range(0, m):
	temp = 0
	for y in range(0, n):
		temp = temp + int(live_lst[x][y])
	
	if temp > 0:
		res += temp

print(res)