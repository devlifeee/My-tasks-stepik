print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = x and ( not (y) and (z) and not (w) and (y) and not (z) )
                if F == 0:
                        print(x, y, z, w)