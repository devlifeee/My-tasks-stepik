#Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

#Вашей программе на вход подается последовательность строк.
#Первая строка содержит число n (1 ≤ n ≤ 100).
#В следующих n строках содержится по одному целому числу.

#Выведите одно число – сумму данных n чисел.

#Примечание:
#﻿Чтобы считать одно число из стандартного потока ввода, можно использовать, например, следующий код

#n = int(input())

n = int(input())
sum = 0 
if 1 <= n <= 100:
    for i in range(n):
        number = int(input())
        sum += number    
print(sum)
