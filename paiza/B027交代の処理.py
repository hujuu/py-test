
dat = input().split()

h = dat[0]
w = dat[1]
n = int(dat[2])

setting = []

for x in range(0, int(h)):
	sets = input().split()
	setting.append(sets)

record = int(input())

record_lst = []

for y in range(0, record):
	records = input().split()
	record_lst.append(records)

ply = []

for player in range(0, n):
	ply.append(player)

score = []

playing = 0

for z in range(0, record):
	row1 = int(record_lst[z][0])-1
	calum1 = int(record_lst[z][1])-1
	
	row2 = int(record_lst[z][2])-1
	calum2 = int(record_lst[z][3])-1

	if z == 0:
		playing = 0
		score.append(0)
	
	if setting[row1][calum1] == setting[row2][calum2]:
		score[playing] = score[playing] + 2
	else:
		playing = playing + 1
		if playing > n-1:
			playing = 0
		try:
			if score[playing] is None:
				score.append(0)
		except IndexError:
			score.append(0)

for out in range(0, n):
	print(score[out])
