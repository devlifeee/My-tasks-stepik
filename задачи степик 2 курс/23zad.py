#s = input()
#a = i = 0
#out = ""
#while i < len(s):
#    if s[i] == s[i + 1]:
#        n += 1
#        i += 1
#    else:
#       s[i] == s[i - 1]
    
stroka = input()
a = i = 0
out = ""
while i < len(stroka)-1:
    if stroka[i] == stroka[i+1]:
        a += 1
        i += 1
    else:
        out += stroka[i] + str(a+1)
        a = 0
        i +=1
else:
    out += stroka[i] + str(a+1)
    
print(out)
