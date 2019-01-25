snakes = [[]] * 10
print(snakes)
#snakes[1].append('蛇')
snakes[1] = ['蛇']
print(snakes)

snakes = [[] for _ in range(10)]
print(snakes)
snakes[1].append('蛇')
print(snakes)