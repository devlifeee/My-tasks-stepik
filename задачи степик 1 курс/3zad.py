def closest_mod_5(x):
    for y in range(1,1000):
        if y >= x and y % 5==0:
            return y
        else:
            y+=1