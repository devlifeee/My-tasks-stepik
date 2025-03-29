#Напишите программу, которая получает на вход три целых числа, 
#по одному числу в строке, и выводит на консоль в три строки 
#сначала максимальное, потом минимальное, после чего оставшееся число.


a = int(input())
b = int(input())
c = int(input())
print(max_number = max(a, b, c))
print(min_number = min(a, b, c)) 
if a > min_number and a < min_number:
    print(a)
if b > min_number and b < min_number:
    print(b)
if c > min_number and c < min_number:
    print(c)

    for n in range(9999, -9999, -1):
    x1 = n // 1000 + n // 100 % 10
    x2 = n // 10 % 10 + n % 10 
    a1 = min(x1, x2)
    a2 = max(x1, x2)
    if a1 == 1 and a2 == 17:
        print(n)
        break
