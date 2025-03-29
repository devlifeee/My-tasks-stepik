n = 0
for n in range(1000, 3000):
    a = n  // 1000
    if a // 2 == 0 and  n % 3 == 0:
        print(n)
        