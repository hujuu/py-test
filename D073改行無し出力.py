import sys

word = input()

word_len = len(word)

for x in range(0, word_len):
	sys.stdout.write(word[word_len-1-x])