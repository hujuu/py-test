all_scores = input()

border_line = int(input())

score_sp = all_scores.split()

res = 0

for cnt in range(7):
	res = res + int(score_sp[cnt])
	
ave = res/7

if ave >= border_line:
	print("pass")
else:
	print("failure")
