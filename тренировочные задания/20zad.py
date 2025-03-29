for n in range(9999, -9999, -1):
    x1 = n // 1000 + n // 100 % 10
    x2 = n // 10 % 10 + n % 10 
    a1 = min(x1, x2)
    a2 = max(x1, x2)
    if a1 == 11 and a2 == 15:
        print(n)
        break