nombres = [1,1,1,2,2,3,4,5,7,7,8,8,8]
num = []
for n in nombres:
    if n not in num:
        num.append(n)
print(num)