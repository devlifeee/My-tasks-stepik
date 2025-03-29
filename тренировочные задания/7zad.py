n = int(input())
if n < 10 and n > 99:
    print("ERROR")
else:
    n = str(n)
    a = str(n[0])
    b = str(n[1])
if a > b:
    print(a, b)
else:
    print(b, a)
