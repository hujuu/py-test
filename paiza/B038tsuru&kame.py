#全体をつると仮定する → かめの匹数を求める
# 	(実際の足の数-匹数の合計×2)÷2=かめの匹数

#全体をかめと仮定する → つるの匹数を求める
# 	(匹数の合計×4-実際の足の数)÷2=つるの匹数

dat = input().split()

foot_all = int(dat[0])
head_all = int(dat[1])
tsuru = int(dat[2])
kame = int(dat[3])

tsuru_search = foot_all - head_all * tsuru
kame_search = head_all * kame - foot_all

res_tsuru = 0
res_kame = 0

if tsuru_search > 0:
	res_tsuru = tsuru_search/2
elif tsuru_search == 0:
	if tsuru == 1:
		res_tsuru = 1
	else:
		res_tsuru = -1

if kame_search > 0:
	res_kame = kame_search/2
elif kame_search == 0:
	if kame == 1:
		res_kame = 1
	else:
		res_kame = -1
	
if res_tsuru < 1:
	print("miss")
elif res_kame < 1:
	print("miss")
else:
	print(int(res_kame), int(res_tsuru))