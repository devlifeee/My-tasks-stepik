#На пульте дистанционного управления есть 4 кнопки.
#Каждая может быть в одном из двух положений - нажата (обозначается единицей) 
#и не нажата (обозначается нулем). Дверь открывается, если нажаты хотя 
#бы две любые кнопки и они находятся не рядом друг с другом. 

#Выведите все возможные комбинации кнопок в виде последовательности 0 и 1, при
#которых двери будут открываться.

#Программа должна выводить в терминал n строк, где n - количество возможных комбинаций.
#В каждой из n таких строк должна быть записана последовательность из 4-х нулей или единиц, разделенных пробелами.
for k1 in range(2): 
    for k2 in range(2):
        for k3 in range(2):
            for k4 in range(2):
               if (k1 + k2 + k3 + k4 >= 2) and((k1 + k2 != 2) and (k2 + k3 != 2) and (k3 + k4 != 2)):
                    print(k1, k2, k3, k4)