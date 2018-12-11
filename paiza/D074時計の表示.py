hour = int(input())

if hour > 47:
	res_hour = hour - 48
	print(res_hour)
elif hour > 23:
	res_hour = hour - 24
	print(res_hour)
else:
	print(hour)