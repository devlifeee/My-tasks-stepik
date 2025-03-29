s = input()
new_s = s[0]
for i in range(1, len(s)):   
    if s[i] == " " and new_s[-1] == " ":       
        pass   
    else:       
        new_s += s[i]
print(new_s)

