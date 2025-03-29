res = []
for x in range(1, 10001):
    if x**5 - 15*x**4 + 85*x**2 - 225*x**2 + 274*x - 120 == 0:
        res.append(x)
res.sort()
print(res)