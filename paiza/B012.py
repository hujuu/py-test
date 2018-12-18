n = int(input())
credit_lst = []

for x in range(0, n):
	credit = input()
	credit_lst.append(credit)

even_lst = [0,2,4,6,8,10,12,14]
odd_lst = [1,3,5,7,9,11,13]

for count in range(0, n):
	even_sum = 0
	odd_sum = 0
	
	for x in even_lst:
		num = []
		temp_even = int(credit_lst[count][x]) * 2
		if temp_even >= 10:
			temp_even = str(temp_even)
			temp_even = int(temp_even[0]) + int(temp_even[1])

		even_sum = even_sum + temp_even

	for x in odd_lst:
		odd_sum = odd_sum + int(credit_lst[count][x])

	res = (even_sum + odd_sum)%10
	if res == 0:
		print(res)
	else:
		print(10 - res)