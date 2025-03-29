#a = "123"
#b = "42"
#print(a + b)
import math
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c)/ 2
s2 = p*(p - a)*(p - b)*(p - c)

print(math.sqrt(s2))
