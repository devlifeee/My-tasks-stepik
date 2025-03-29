count =  0
for m in range(1, 20, 2):
    for n in range(1, 20, 2):
        for k in range(1, 20, 2):
            if 3000000 <= (3**m) * (4**n) * (5**k) >= 4000000:
                count += 1
print(count)