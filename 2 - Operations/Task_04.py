lis = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
min = max = lis[0]
for l in lis:
    if l > max:
        max = l
    if l < min:
        min = l
print(min,max)