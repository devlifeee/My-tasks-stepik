# Напишите функцию update_dictionary которая принимает на вход словарь d и два числа: key и value.
# Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key Если и ключа 
# 2∗key нет, то нужно добавить ключ 2∗key в словарь и сопоставить ему список из переданного элемента[value]

#def update_dictionary(d, key, value):
#   if key  in d:
#       d[key] = value
#    else:
#       d[key] = 2 * [key]

def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]