#Вернувшись домой, Ник обнаружил, что Алгоритм появился на рабочем столе его собственного компьютера!
#
#Это образец работал так: он получает на вход четырёхзначное число. 
#По этому числу строится новое число по следующим правилам
#1.  Складываются отдельно первая и вторая цифры, вторая и третья цифры,
#а также третья и четвёртая цифры.
#
#2.  Из полученных трёх чисел выбираются два наибольших и записываются друг за другом в порядке неубывания 
#(без разделительных символов).
#
#Напишите программу, которая вычисляет и выводит в терминал наименьшее число, 
#при обработке которого автомат выдаёт результат 1418
for i in range(1000, 10000):
    s = str(i)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    first = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3))
    second = str(max(k1, k2, k3))
    s1 = first + second
    if s1 == '1418':
        print(i)
        break
