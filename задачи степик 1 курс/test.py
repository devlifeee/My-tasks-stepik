#x = [1, 2, 3]
#y  = x 
#y is x
#y is [1, 2, 3]
#print(x)
#x = [1, 2, 3]
#y = x
#print(id(x)) #id одинаковые
#print(id(y)) #id одинаковые
x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s)