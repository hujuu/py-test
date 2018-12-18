card = input()
card = card.split()
numberList = [card[i] for i in range(4)]

numberList.sort()
result = int(numberList[0]) + int(numberList[1]) + (int(numberList[2]) + int(numberList[3])) * 10
print(result)
