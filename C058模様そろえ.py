question = input()
question = question.split()
word_len = int(question[0])

states = question[2]

res = question[1]

for count in range(word_len):
    if res != states:
        states = states[1:] + states[0]
    else:
        print(count)
        break
