sentence = input()

se_len = len(sentence)

res = ""

for n in range(se_len):
    res = res + sentence[se_len - n - 1]

print(res)
