card = input()
card = card.split()
start_price = int(card[0])
a_budget = int(card[1])
b_budget = int(card[2])

temp = start_price

while a_budget >= temp:
	temp += 10
	if temp + 1000 <= b_budget:
		temp += 1000
	else:
		break

if temp + 1000 >= b_budget and temp < a_budget:
	print("A", temp)
elif temp <= b_budget:
	print("B", temp)
