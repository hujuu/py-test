list_with_dupes = [1,5,6,2,5,6,8,3,8,3,3,7,9]

# 重複する値を排除する
set_without_dupes = set(list_with_dupes)

print(set_without_dupes)

first_set = set([1,5,6,2,6,3,6,7,37,9,10,321,54,654,432])

second_set = set([4,6,7,432,6,7,4,9,0])

# 積集合
print(first_set.intersection(second_set))

# 和集合
print(first_set.union(second_set))

# 差集合
print(first_set.difference(second_set))

print(second_set - first_set)

print(6 in second_set)
print(0 in first_set)

import numpy as np

print(np.unique(list_with_dupes, return_index = True))

from fuzzywuzzy import fuzz

my_records = [{'book': 'Grapes of Wrath'},{'book': 'The Grapes of Wrath'}]

print(fuzz.ratio(my_records[0].get('book'), my_records[1].get('book')))

print(fuzz.partial_ratio(my_records[0].get('book'), my_records[1].get('book')))
