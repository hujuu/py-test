party = int(input())

cards = input()
cards_split = cards.split()
ten = "x10" in cards_split

bonus = 1

if ten is True:
    cards_split.remove("x10")
    bonus = 10

cards_split_i = [int(s) for s in cards_split]

zero = "0" in cards_split

if zero is True:
    max_num = max(cards_split_i)
    cards_split_i.remove(max_num)

res = sum(cards_split_i) * bonus

print(res)
