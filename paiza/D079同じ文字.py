password = input()

cnt = len(password)

words = []


def word_to_list(count, word):
	word_list = []
	
	for loop in range(count):
		word_list.append(word[loop])
	
	return word_list


words = word_to_list(cnt, password)

print(words)

for x in range(cnt - 1):
	if words[x] != words[x + 1]:
		print("OK")
		break
	elif x == cnt - 2:
		print("NG")
