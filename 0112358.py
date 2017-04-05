# 斐波那契数列
def f(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return b

for i in range(10):
   print(f(i))
