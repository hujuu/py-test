import collections

n = int(input())

dat = input().split()

count_dict = collections.Counter(dat)

#print(count_dict)
#max_key = max(count_dict.items(), key=lambda x:x[1])[0]

# valueがmaxであるkeyを探してくる
max_val = max(count_dict.values())
keys_of_max_val = [key for key in count_dict if count_dict[key] == max_val]

res = sorted(keys_of_max_val)

print(' '.join(res))