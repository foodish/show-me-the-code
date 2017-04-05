# 概率试验
import random


l = []

n = int(input('请输入试验次数:'))
for i in range(n):
    a = range(1, 11)
    b = random.choice(a)
    l.append(b)
        
for j in set(l):
    print(n, '次试验中', j, '出现的概率为', l.count(j) / n)

# l = [x for x in random.choice(range(1, 11))]


