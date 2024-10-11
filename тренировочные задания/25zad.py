for y  in "01234567":
    for x  in "01234567":
        t = int("77" + x + "3" + y, 8) + int("6" +  x  + "22" + y, 11)
        if t % 51 == 0:
            print(t // 51)
            break
        