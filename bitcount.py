nm = input()

nm_split = nm.split()

n = int(nm_split[0])
m = int(nm_split[1])

def bc(x):
	return bin(x).count("1")

lst = []
res = 0

for cnt in range(0, n+1):
	if bc(cnt) == m:
		res = res + 1

print(res)
