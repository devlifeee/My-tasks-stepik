#Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
#первое число, второе число и операцию, после чего применяет операцию к введённым числам 
#("первое число" "операция" "второе число") и выводит результат на экран.
#
#Поддерживаемые операции: +, -, /, *, mod, pow, div, где
#mod — это взятие остатка от деления,
#pow — возведение в степень,
#div — целочисленное деление.
#
#Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#
#Обратите внимание, что на вход программе приходят вещественные числа.

a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = input("Операция: ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Деление на 0!")
elif c == "*":
    print(a * b)
elif c == "mod":
    if b != 0:
        print(a % b)
    else:
        print("Деление на 0!")
elif c == "pow":
    print(a ** b)
elif c == "div":
    if b != 0:
        print(a // b)
    else:
        print("Деление на 0!")


