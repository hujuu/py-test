import re

input_date = input()


def format_text(text):
    text = re.sub(' ', "", text)
    return text


md = format_text(input_date)

for check in range(len(md) - 1):
    # print(md[check])
    # print(check)
    if md[check] != md[check + 1]:
        print("No")
        break
    if check == len(md) - 2:
        print("Yes")
