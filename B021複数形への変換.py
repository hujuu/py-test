num = int(input())
words = [input() for i in range(num)]

es = ['s', 'sh', 'ch', 'o', 'x']
ves = ['f', 'fe']
ies = ['a', 'i', 'u', 'e', 'o']

for count in range(num):
	if words[count][-1:] in es:
		words[count] = words[count] + "es"
		print(words[count])
	elif words[count][-2:] in es:
		words[count] = words[count] + "es"
		print(words[count])
	elif words[count][-1:] in ves:
		words[count] = words[count][:-1] + "ves"
		print(words[count])
	elif words[count][-2:] in ves:
		words[count] = words[count][:-2] + "ves"
		print(words[count])
	elif words[count][-1:] == "y":
		if words[count][-2:-1] not in ies:
			words[count] = words[count][:-1] + "ies"
			print(words[count])
		else:
			words[count] = words[count] + "s"
			print(words[count])
	else:
		words[count] = words[count] + "s"
		print(words[count])
	