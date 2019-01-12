import numpy as np
import time


start = time.time()
data1 = [6, 7.5, 8, 0, 1]

arr1 = np.array(data1)

print(arr1)

print(np.empty((2, 3, 2)))


all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

names_of_interest = []

for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)

# ネストしたリスト内包表記を使えば、この操作を 1 行で次のように書けます。
result = [name for names in all_data for name in names if name.count('e') >= 2]

print(names_of_interest)
print(result)

elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
