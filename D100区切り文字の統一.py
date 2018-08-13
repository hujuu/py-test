word = input()

under = word.count('_')
bar = word.count('-')


if int(under) >= int(bar):
    dst = word.replace('-', '_')
else:
    dst = word.replace('_', '-')

print(dst)


