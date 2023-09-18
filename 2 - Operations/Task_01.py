list = []
for i in range(10):
    list.append(i+1)
print(list)
res = 1
for l in list:
    res *= l
print(res)