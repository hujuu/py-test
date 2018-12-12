member = int(input())
name = input()
names = name.split()

book = int(input())
buy = [input() for i in range(book)]

dic = {}

for members in range(member):
	dic[names[members]] = 0

for books in buy:
	temp = books.split()
	dic[temp[0]] += int(temp[1])
	
for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
	print(k)