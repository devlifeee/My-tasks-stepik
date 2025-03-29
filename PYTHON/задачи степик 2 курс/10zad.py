#Жители страны Малевии часто экспериментируют с планировкой комнат.
#Комнаты бывают треугольные, прямоугольные и круглые. 
#Чтобы быстро вычислять жилплощадь, требуется написать программу, 
#на вход которой подаётся тип фигуры комнаты и соответствующие параметры, 
#которая бы выводила площадь получившейся комнаты.
#Для числа π в стране Малевии используют значение 3.14.
# put your python code here
import math
name = str(input())
if name == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p=(a+b+c)/2
    print(p)
elif name == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)
elif name == "круг":
    r = float(input())
    print(3.14 * r ** 2)

import math
t = str (input())
if t =='треугольник':
    a = int (input())
    b = int (input())
    c = int (input())
    p = (a+b+c)/2
    S = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print(S)
elif t =='прямоугольник':
    a = int (input())
    b = int (input())
    S = a * b
    print(S)
elif t =='круг':
    r = int (input())
    S = 3.14 * r**2
    print(S)
