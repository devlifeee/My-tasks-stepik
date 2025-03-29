row = int(input())
column = int(input())
for i in range(3):
    for j in range(3):
        if i == row and j == column:
            if j == 2:
                print("X")
            else:
                print("X", end="")
        else:           
            if j == 2:               
                print("*")           
            else:               
                print("*", end="")


print(" 1 число: a, 2 число: b, 3 число: c, 4 число: d")