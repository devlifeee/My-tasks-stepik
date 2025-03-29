a = int(input())
b = int(input())
c = int(input())
nums = [a, b, c]
result = []
for i in nums:   
    for j in nums:       
        for g in nums:           
            if i != 0:               
                result.append(str(i) + str(j) + str(g))
result.sort()
print(result)