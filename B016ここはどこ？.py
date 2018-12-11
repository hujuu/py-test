setting = input()
set_data = setting.split()

width = int(set_data[0])
height = int(set_data[1])
count = int(set_data[2])

first_position = input()
first_point = first_position.split()
start = [int(first_point[0]), int(first_point[1])]

action = [input() for i in range(count)]

dic = {}
forward_list = ["U", "D", "R", "L"]

for dic_key in forward_list:
	dic[dic_key] = 0

for actions in action:
	temp = actions.split()
	dic[temp[0]] += int(temp[1])

move = [dic['R']-dic['L'], dic['U']-dic['D']]

x_ans = start[0] + move[0]

if x_ans > width:
	x_ans -= width
	
if x_ans < 0:
	x_ans += width

y_ans = start[1] + move[1]

if y_ans > height:
	y_ans -= height

if y_ans < 0:
	y_ans += height

print(x_ans, y_ans)
