setting = input()
set_data = setting.split()

res = 0

for cnt in range(len(set_data)):
	res += int(set_data[cnt])
	
print(str(res)[-1:])
