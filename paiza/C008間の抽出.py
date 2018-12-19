import re

tags = input().split()
words = input()

s = words.find(tags[0])
t = words.rfind(tags[1])

s2 = s + len(tags[0])

split0 = words.split(tags[0])

for x in range(0, len(split0)):
	u = split0[x].find(tags[1])
	if u > 0:
		print(split0[x][0:u])
	elif u == 0:
		print('<blank>')