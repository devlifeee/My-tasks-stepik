# Напишите программу, которая считывает со стандартного ввода целые числа,
# по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

#for i in range(a, b):
#    sum = 0
#    while a or b == 0:
#        sum = a + b
#        print(sum)
#        break
sum = 0
number = int(input())

while number != 0:
  sum += number
  number = int(input())

print(sum)
