import re

word = '\w+'

sentence = 'Here is my sentence'

find_all = re.findall(word, sentence)

print(find_all)

seach_res = re.search(word, sentence)

print(seach_res)

sg = seach_res.group()

print(sg)

sg = seach_res.group(0)

print(sg)

match_res = re.match(word, sentence)

print(match_res)

number = '\d+'
capitalized_word = '[A-Z]\w+'

sentence = 'I have 2 pets: Bear and Bunny.'

seach_num = re.search(number, sentence)

print(seach_num)