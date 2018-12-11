two_num = input()

nums = two_num.split()

res = int(nums[0]) * int(nums[1])

if res > 10000:
	print("NG")
else:
	print(res)
