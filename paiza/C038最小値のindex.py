setting = input()
setting = setting.split()

n = int(setting[0])
balls = int(setting[1])

machine_lst = []

for x in range(0, n):
	machines = int(input())
	machine_lst.append(machines)
	
machine_rest = []

for x in range(0, n):
	rest = balls % machine_lst[x]
	machine_rest.append(rest)

print (max([i for i, x in enumerate(machine_rest) if x == min(machine_rest)])+1)