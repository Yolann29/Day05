import time
import random
startingTime = time.time()
lis = []
for i in range(10**6):
    lis.append(random.randint(0,10**6))
lis.sort()
duration = time.time() - startingTime
print(duration)